from datetime import datetime
from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface
from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.storages.configure_slot_storage_interface \
    import ConfigureSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.dtos.dtos import PreviousSlotDto
from slot_booking.constants.enums import Day
from datetime import datetime

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


    def valid_date_details(self, user_id: int, date: str):

        present_date = str(datetime.now().date())
        is_not_valid_date_to_book =  date < present_date

        if is_not_valid_date_to_book:
            self.presenter.raise_exception_for_invalid_date()
            return False

        book_no_of_days_after = self.configure_slot_storage.book_no_of_days_after()
        is_user_cannot_book_in_date = self.user_slot_storage.cannot_book_in_date(
            user_id, present_date, book_no_of_days_after)

        if is_user_cannot_book_in_date:
            self.presenter.raise_exception_for_cannot_book_in_date()
            return False

        return True


    def get_day(self, date: str):
        days = [day.value for day in Day]
        date_object = datetime.strptime(date, "%Y-%m-%d")
        day = date_object.strftime("%A")

        slots_unavailable = day not in days
        if slots_unavailable:
            self.presenter.slot_not_booked_response()
            return False

        return day


    def valid_time_slots(self, day: str, start_time: str, end_time: str):

        washing_machines = \
            self.washing_machine_slot_storage.washing_machines_in_given_slot(
            day, start_time, end_time
        )

        is_invalid_start_time = "start_time" in washing_machines
        if is_invalid_start_time:
            self.presenter.raise_exception_for_invalid_start_time()
            return False

        is_invalid_end_time = "end_time" in washing_machines
        if is_invalid_end_time:
            self.presenter.raise_exception_for_invalid_end_time()
            return False

        return washing_machines


    def book_a_slot(self, user_id: int, date: str, start_time: str, 
        end_time: str):

        not_valid_date_details_to_book = self.valid_date_details(
            user_id=user_id, date=date)

        if not_valid_date_details_to_book:
            return

        invalid_day = self.get_day(date=date)
        if invalid_day:
            return

        day = invalid_day
        invalid_time_slot = self.valid_time_slots(day=day, 
            start_time=start_time, end_time=end_time
            )

        if invalid_time_slot:
            return 

        washing_machines = invalid_time_slot

        slot_booked = self.user_slot_storage.create_user_slot(
            user_id, date, start_time, end_time, washing_machines
        )

        if slot_booked:
            slot_response =  self.presenter.slot_booked_response()
        else:
            slot_response = self.presenter.unavailable_washing_machines_response()

        return slot_response



'''


    def book_a_slot(self, user_id: int, date: str, start_time: str, 
        end_time: str):

        present_date = str(datetime.now().date())
        is_not_valid_date_to_book =  date < present_date

        if is_not_valid_date_to_book:
            self.presenter.raise_exception_for_invalid_date()
            return

        book_days_after = self.configure_slot_storage.book_days_after()
        is_user_invalid_date_to_book = self.user_slot_storage.cannot_book_in_date(
            user_id, present_date, book_days_after)

        if is_user_invalid_date_to_book:
            self.presenter.raise_exception_for_cannot_book_in_date()
            return

        date_object = datetime.strptime(date, "%Y-%m-%d")
        day = date_object.strftime("%A")

        days = [day.value for day in Day]
        slots_unavailable = day not in days
        if slots_unavailable:
            self.presenter.slot_not_booked()
            return

        washing_machines = \
            self.washing_machine_slot_storage.washing_machines_in_given_slot(
            day, start_time, end_time
        )

        is_invalid_start_time = "start_time" in washing_machines
        if is_invalid_start_time:
            self.presenter.raise_exception_for_invalid_start_time()
            return

        is_invalid_end_time = "end_time" in washing_machines
        if is_invalid_end_time:
            self.presenter.raise_exception_for_invalid_end_time()
            return

        slot_booked = self.user_slot_storage.create_user_slot(
            user_id, date, start_time, end_time, washing_machines
        )

        if slot_booked:
            slot_response =  self.presenter.slot_booked()
        else:
            slot_response = self.presenter.raise_exception_for_unavailable_washing_machines()
        
        return slot_response


'''