from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface    
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.constants.enums import Day

class WashingMachineSlotsInteractor:

    def __init__(self, 
        washing_machine_slot_storage: WashingMachineSlotStorageInterface,
        washing_machine_storage: WashingMachineStorageInterface,
        presenter: PresenterInterface):

        self.washing_machine_storage = washing_machine_storage
        self.washing_machine_slot_storage = washing_machine_slot_storage
        self.presenter = presenter

    def get_washing_machine_slots(self, day: str, washing_machine_id: str):

        days = [day.value for day in Day]

        is_invalid_washing_machine_id = \
            not self.washing_machine_storage.is_valid_washing_machine_id(
                washing_machine_id)

        if is_invalid_washing_machine_id:
            self.presenter.raise_exception_for_invalid_washing_machine_id()
            return

        is_invalid_day = day not in days

        if is_invalid_day:
            self.presenter.raise_exception_for_invalid_day()
            return

        washing_machine_slots_dto= \
        self.washing_machine_slot_storage.get_washing_machine_slots( 
            day=day, washing_machine_id=washing_machine_id
        )

        response =  self.presenter.get_response_for_washing_machine_slots(
            washing_machine_slots_dto)

        return response
