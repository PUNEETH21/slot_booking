from datetime import datetime, date , time
from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.dtos.dtos import PreviousSlotDto


class PreviousSlotsInteractor:

    def __init__(self,
        user_slot_storage: UserSlotStorageInterface,
        presenter: PresenterInterface):

        self.user_slot_storage = user_slot_storage
        self.presenter = presenter


    def is_previous_slot(self, user_slot_dto, present_time):
        previous_slot = user_slot_dto.end_time < present_time

        return previous_slot


    def previous_slots(self, user_slots_dtos):
        previous_slot_dto_list = []
        today_date = str(datetime.now().date())
        present_time = str(datetime.now().time())
        for user_slot_dto in user_slots_dtos:
            is_today = user_slot_dto.date == today_date
            if is_today:
                is_previous_slot = self.is_previous_slot(
                    user_slot_dto, present_time
                )
            else:
                is_previous_slot = True

            if is_previous_slot:
                previous_slot_dto_list.append(
                    PreviousSlotDto(
                        date = str(user_slot_dto.date),
                        start_time = str(user_slot_dto.start_time),
                        end_time = str(user_slot_dto.end_time),
                        washing_machine_id=user_slot_dto.washing_machine_id
                    )
                )

        return previous_slot_dto_list


    def get_previous_slots(self, user_id: int):

        user_slots_dtos = self.user_slot_storage.get_previous_slots(
            user_id=user_id)
        
        if user_slots_dtos:
            previous_slots_dtos = self.previous_slots(user_slots_dtos)
        else:
            previous_slots_dtos = []

        previous_slots = self.presenter.get_response_for_previous_slots(
            previous_slots_dtos)

        return previous_slots
