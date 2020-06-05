from unittest.mock import create_autospec

from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface

from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.washing_machine_slots_interactor import \
    WashingMachineSlotsInteractor

from django_swagger_utils.drf_server.exceptions import NotFound
import pytest

pytestmark = pytest.mark.django_db

def test_get_washing_machine_slots_invalid_washing_machine_id_raise_exceptions():
    #Arrange
    washing_machine_id = "wm1"
    day = "Monday"

    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    washing_machine_storage = create_autospec(WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = WashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = False
    presenter.raise_exception_for_invalid_washing_machine_id.side_effect = \
        NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.get_washing_machine_slots(
            day=day,
            washing_machine_id=washing_machine_id
        )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id)
    presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once_with()

def test_get_washing_machine_slots_invalid_day_raise_exceptions():
    #Arrange
    washing_machine_id = "wm1"
    day = "Monda"

    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    washing_machine_storage = create_autospec(WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = WashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    presenter.raise_exception_for_invalid_day.side_effect = \
        NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.get_washing_machine_slots(
            day=day,
            washing_machine_id=washing_machine_id
        )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id)
    presenter.raise_exception_for_invalid_day.assert_called_once_with()



def test_get_washing_machine_slots_interactor_returns_washing_machine_slots_dto(
    washing_machine_slots_dtos):
    #Arrange
    washing_machine_id = "wm1"
    day = "Monday"
    expected_output = {
      "washing_machine_slots":  [
            {
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
            },
            {
                "start_time": "20:22:46.810366",
                "end_time": "21:22:46.810366",
            }
        ]
    }

    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    washing_machine_storage = create_autospec(WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = WashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )
    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    washing_machine_slot_storage.get_washing_machine_slots.return_value = \
        washing_machine_slots_dtos
    presenter.get_response_for_washing_machine_slots.return_value = expected_output

    #Act
    response = interactor.get_washing_machine_slots(
        day=day,
        washing_machine_id=washing_machine_id
    )

    #Assert
    washing_machine_slot_storage.get_washing_machine_slots.assert_called_once_with(
        day=day, washing_machine_id=washing_machine_id)
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id)
    presenter.get_response_for_washing_machine_slots.assert_called_once_with(
        washing_machine_slots_dtos)
    assert response == expected_output


def test_get_washing_machine_slots_interactor_returns_washing_machine_slots_dto_empty(
    washing_machine_slots_dtos):
    #Arrange
    washing_machine_id = "wm1"
    day = "Monday"

    expected_output = {
      "washing_machine_slots":  []
    }

    washing_machine_slots_dtos = []

    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    washing_machine_storage = create_autospec(WashingMachineStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = WashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    washing_machine_slot_storage.get_washing_machine_slots.return_value = \
        washing_machine_slots_dtos
    presenter.get_response_for_washing_machine_slots.return_value = expected_output

    #Act
    response = interactor.get_washing_machine_slots(
        day=day,
        washing_machine_id=washing_machine_id
    )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
    washing_machine_id)
    washing_machine_slot_storage.get_washing_machine_slots.assert_called_once_with(
        day=day, washing_machine_id=washing_machine_id)
    presenter.get_response_for_washing_machine_slots.assert_called_once_with(
        washing_machine_slots_dtos)
    assert response == expected_output

