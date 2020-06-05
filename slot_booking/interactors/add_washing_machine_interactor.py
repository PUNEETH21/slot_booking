from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface    
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

class AddWashingMachineInteractor:

    def __init__(self,
        washing_machine_storage: WashingMachineStorageInterface,
        presenter: PresenterInterface):

        self.washing_machine_storage = washing_machine_storage
        self.presenter = presenter

    def add_washing_machine(self, washing_machine_id: str):

        washing_machine_id_already_exist = \
            self.washing_machine_storage.is_valid_washing_machine_id(
            washing_machine_id
        )

        if washing_machine_id_already_exist:
            self.presenter.raise_exception_for_washing_machine_id_already_exist()
            return

        is_active = True
        self.washing_machine_storage.add_washing_machine(
                washing_machine_id, is_active
        )

        response = self.presenter.get_response_for_add_washing_machine()
        return response
