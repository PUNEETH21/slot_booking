from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface    
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.exceptions.exceptions import \
     WashingMachineIdAlreadyExist

class AddWashingMachineInteractor:

    def __init__(self,
        washing_machine_storage: WashingMachineStorageInterface
        ):

        self.washing_machine_storage = washing_machine_storage


    def add_washing_machine_wrapper(self,
        washing_machine_id:str, presenter: PresenterInterface):

        try:
            self.add_washing_machine(washing_machine_id)
        except WashingMachineIdAlreadyExist:
            presenter.raise_exception_for_washing_machine_id_already_exist()
            return

        response = presenter.get_response_for_add_washing_machine()
        return response


    def add_washing_machine(self, washing_machine_id: str):

        washing_machine_id_already_exist = \
            self.washing_machine_storage.is_valid_washing_machine_id(
            washing_machine_id
        )

        if washing_machine_id_already_exist:
            raise WashingMachineIdAlreadyExist

        is_active = True
        self.washing_machine_storage.add_washing_machine(
                washing_machine_id, is_active
        )

        return

