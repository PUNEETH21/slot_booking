from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface    
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

class GetWashingMachineDetailsInteractor:

    def __init__(self,
        washing_machine_storage: WashingMachineStorageInterface,
        presenter: PresenterInterface):

        self.washing_machine_storage = washing_machine_storage
        self.presenter = presenter

    def get_washing_machine_details(self, washing_machine_id: str):
        print("#"*22)
        invalid_washing_machine_id = \
            not self.washing_machine_storage.is_valid_washing_machine_id(
            washing_machine_id
        )

        if invalid_washing_machine_id:
            self.presenter.raise_exception_for_invalid_washing_machine_id()
            return

        washing_machine_details_dto = \
            self.washing_machine_storage.get_washing_machine_details(
            washing_machine_id
        )

        response = self.presenter.get_response_for_get_washing_machine_details(
            washing_machine_details_dto
        )

        return response
