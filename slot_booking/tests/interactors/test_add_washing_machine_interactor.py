from unittest.mock import create_autospec

from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.add_washing_machine_interactor import \
    AddWashingMachineInteractor

from django_swagger_utils.drf_server.exceptions import BadRequest
import pytest

pytestmark = pytest.mark.django_db

def test_add_get_washing_machine_interactor_raise_exception_washing_machine_id_already_exist():
    #Arrange
    washing_machine_id = "wm1"
    is_active = True
    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AddWashingMachineInteractor(
        washing_machine_storage=washing_machine_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    presenter.raise_exception_for_washing_machine_id_already_exist.side_effect = \
        BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.add_washing_machine(
            washing_machine_id=washing_machine_id
        )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )

    presenter.raise_exception_for_washing_machine_id_already_exist.assert_called_once_with()


def test_add_washing_machine_interactor_return_created_response():
    #Arrange
    washing_machine_id = "wm1"
    expected_response = "Washing Machine Added Successfully"
    is_active = True
    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AddWashingMachineInteractor(
        washing_machine_storage=washing_machine_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = False
    presenter.get_response_for_add_washing_machine.return_value = \
        expected_response

    #Act
    response = interactor.add_washing_machine(
        washing_machine_id=washing_machine_id
    )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )
    washing_machine_storage.add_washing_machine.assert_called_once_with(
        washing_machine_id=washing_machine_id, is_active=is_active
    )
    presenter.get_response_for_add_washing_machine.assert_called_once_with()

    assert response == expected_response
