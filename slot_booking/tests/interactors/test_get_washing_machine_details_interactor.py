from unittest.mock import create_autospec

from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.get_washing_machine_details_interactor import \
    GetWashingMachineDetailsInteractor

from django_swagger_utils.drf_server.exceptions import NotFound
import pytest

pytestmark = pytest.mark.django_db

def test_get_washing_machine_details_interactor_raise_invalid_washing_machine_id():
    #Arrange
    washing_machine_id = "wm1"

    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetWashingMachineDetailsInteractor(
        washing_machine_storage=washing_machine_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = False
    presenter.raise_exception_for_invalid_washing_machine_id.side_effect = \
        NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.get_washing_machine_details(
            washing_machine_id=washing_machine_id
        )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )
    presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once_with()


def test_get_washing_machine_details_interactor_return_washing_machine_details(
    washing_machine_details_dto):
    #Arrange
    washing_machine_id = "wm1"
    expected_response = {
        "washing_machine_id" : "wm1",
        "is_active" : True
    }
    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetWashingMachineDetailsInteractor(
        washing_machine_storage=washing_machine_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    washing_machine_storage.get_washing_machine_details.return_value = \
        washing_machine_details_dto
    presenter.get_response_for_get_washing_machine_details.return_value = \
        expected_response

    #Act
    response = interactor.get_washing_machine_details(
            washing_machine_id=washing_machine_id
    )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )

    washing_machine_storage.get_washing_machine_details.assert_called_once_with(
        washing_machine_id
    )

    presenter.get_response_for_get_washing_machine_details.assert_called_once_with(
        washing_machine_details_dto=washing_machine_details_dto
    )

    assert response == expected_response
