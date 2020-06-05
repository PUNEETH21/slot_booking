from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

class UpdateSlotInteractor:

    def __init__(self, 
        washing_machine_slot_storage: WashingMachineSlotStorageInterface,
        washing_machine_storage: WashingMachineStorageInterface,
        presenter: PresenterInterface):

        self.washing_machine_storage = washing_machine_storage
        self.washing_machine_slot_storage = washing_machine_slot_storage
        self.presenter = presenter

    def update_slot(self, day: str, start_time: str, end_time: str,
        washing_machine_id: str):
        is_invalid_washing_machine_id = \
            not self.washing_machine_storage.is_valid_washing_machine_id(
                washing_machine_id)
        if is_invalid_washing_machine_id:
            self.presenter.raise_exception_for_invalid_washing_machine_id()
            return

        alloted_slots_dto = self.washing_machine_slot_storage.update_slot(
            day=day,
            start_time=start_time,
            end_time=end_time,
            washing_machine_id=washing_machine_id
        )

        response =  self.presenter.get_response_for_alloted_slots(
            alloted_slots_dto)

        return response

