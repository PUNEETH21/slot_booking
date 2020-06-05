from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface
from slot_booking.models.washing_machine import Washingmachine
from slot_booking.dtos.dtos import WashingMachineDetailsDto

class WashingMachineStorageImplementation(
    WashingMachineStorageInterface):

    def is_valid_washing_machine_id(self, washing_machine_id: str):
        washing_machine_obj =Washingmachine.objects.filter(
            washing_machine_id=washing_machine_id)

        if washing_machine_obj:
            return True
        else:
            return False

    def add_washing_machine(self, washing_machine_id: str, is_active: bool):
        Washingmachine.objects.create(
            washing_machine_id=washing_machine_id, is_active=is_active
        )

    def get_washing_machine_details(self, washing_machine_id: str):
        washing_machine_obj = Washingmachine.objects.get(
            washing_machine_id=washing_machine_id
        )

        washing_machine_details_dto = WashingMachineDetailsDto(
            washing_machine_id = washing_machine_obj.washing_machine_id,
            is_active = washing_machine_obj.is_active
        )

        return washing_machine_details_dto


