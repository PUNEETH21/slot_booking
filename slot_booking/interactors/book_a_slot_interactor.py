from datetime import datetime
from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface
from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.storages.configure_slot_storage_interface \
    import ConfigureSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.constants.enums import Day
import time

class BookASlotInteractor:

    def __init__(self,
        washing_machine_slot_storage: WashingMachineSlotStorageInterface,
        user_slot_storage: UserSlotStorageInterface,
        configure_slot_storage: ConfigureSlotStorageInterface,
        presenter: PresenterInterface
    ):

        self.washing_machine_slot_storage = washing_machine_slot_storage 
        self.user_slot_storage = user_slot_storage
        self.configure_slot_storage = configure_slot_storage
        self.presenter = presenter


    def _valid_date_details(self, user_id: int, date: str):

        present_date = datetime.now().date()

        is_not_valid_date_to_book = date < present_date
#        print(present_date, is_not_valid_date_to_book, date)
        if is_not_valid_date_to_book:
            self.presenter.raise_exception_for_invalid_date()
            return False

        book_no_of_days_after = \
            self.configure_slot_storage.book_no_of_days_after()


        user_last_used_date = self.user_slot_storage.last_used_date(
            user_id
        )

#        print(book_no_of_days_after, user_last_used_date)
        is_user_cannot_book_in_date = False
        if user_last_used_date:
            diff_in_days = present_date - user_last_used_date
            is_user_cannot_book_in_date = \
                book_no_of_days_after>=diff_in_days.days

        #print("22"*2, user_last_used_date)
        if is_user_cannot_book_in_date:
            self.presenter.raise_exception_for_cannot_book_in_date()
            return 

        return True


    def _get_day(self, date: str):
        days = [day.value for day in Day]

        day = date.strftime("%A")
        print(day, days)
        no_slots_in_given_date = day not in days
        if no_slots_in_given_date:
            self.presenter.raise_exception_for_no_slots_in_given_date()
            return False

        return day


    def _valid_time_slots(self, day: str, start_time: str, end_time: str):

        washing_machines_ids = \
            self.washing_machine_slot_storage.washing_machines_in_given_slot(
            day, start_time, end_time
        )
#        print(day, start_time, end_time, washing_machines_ids)
        no_washing_machine_slots = not washing_machines_ids
        if no_washing_machine_slots:
            self.presenter.raise_exception_for_invalid_time_slot()
            return False

        return washing_machines_ids


    def book_a_slot(self, user_id: int, date: str, start_time: str, 
        end_time: str):

        print("a"*20, "login")
        not_valid_date_details_to_book = not self._valid_date_details(
            user_id=user_id, date=date)

        if not_valid_date_details_to_book:
            return


        day = self._get_day(date=date)
        invalid_day = not day
        #print("b"*20, not_valid_date_details_to_book, invalid_day)
        if invalid_day:
            return
        print("b"*20, not_valid_date_details_to_book, invalid_day)

        washing_machines_ids = self._valid_time_slots(day=day, 
            start_time=start_time, end_time=end_time
        )

        invalid_time_slots = not washing_machines_ids

        if invalid_time_slots:
            return 


        slot_booked = self.user_slot_storage.create_user_slot(
            user_id, date, start_time, end_time, washing_machines_ids
        )

        print("33")
        if slot_booked:
            slot_response =  self.presenter.get_response_for_slot_booked()
        else:
            slot_response = \
                self.presenter.get_response_for_unavailable_washing_machines()

        return slot_response

