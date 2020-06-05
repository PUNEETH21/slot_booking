from datetime import datetime, date , time
from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.dtos.dtos import UpcomingSlotDto


class UpcomingSlotsInteractor:

    def __init__(self,
        user_slot_storage: UserSlotStorageInterface,
        presenter: PresenterInterface):

        self.user_slot_storage = user_slot_storage
        self.presenter = presenter


    def is_upcoming_slot(self, user_slot_object, present_time):
        upcoming_slot = user_slot_object.start_time > present_time

        return upcoming_slot


    def upcoming_slots(self, user_slot_objects_dtos):
        upcoming_slot_dto_list = []
        today_date = str(datetime.now().date())
        present_time = str(datetime.now().time())
        for user_slot_object in user_slot_objects_dtos:
            is_today = user_slot_object.date == today_date
            if is_today:
                is_upcoming_slot = self.is_upcoming_slot(
                    user_slot_object, present_time
                )
            else:
                is_upcoming_slot = True

            if is_upcoming_slot:
                upcoming_slot_dto_list.append(
                    UpcomingSlotDto(
                        date = str(user_slot_object.date),
                        start_time = str(user_slot_object.start_time),
                        end_time = str(user_slot_object.end_time),
                        washing_machine_id=user_slot_object.washing_machine_id
                    )
                )

        return upcoming_slot_dto_list


    def get_upcoming_slots(self, user_id: int):

        user_slot_objects_dtos = self.user_slot_storage.get_upcoming_slots(
            user_id=user_id)
        
        if user_slot_objects_dtos:
            upcoming_slots_dtos = self.upcoming_slots(user_slot_objects_dtos)
        else:
            upcoming_slots_dtos = []

        upcoming_slots = self.presenter.get_response_for_upcoming_slots(
            upcoming_slots_dtos)

        return upcoming_slots

