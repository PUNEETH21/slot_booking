from unittest.mock import create_autospec

from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface

from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.update_washing_machine_slots_interactor import \
    UpdateWashingMachineSlotsInteractor

from django_swagger_utils.drf_server.exceptions import BadRequest
import pytest
from unittest.mock import patch

pytestmark = pytest.mark.django_db

def test_update_slots_interactor_raise_exception_for_invalid_day():
    #Arrange
    day = "Sunday"
    washing_machine_id = "wm1"
    time_slots = [
        {
            "start_time" : "06:00",
            "end_time" : "07:00"
        },
        {
            "start_time" : "07:00",
            "end_time" : "08:00"
        },
        {
            "start_time" : "08:00",
            "end_time" : "09:00"
        }
    ]

    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)        
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateWashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    presenter.raise_exception_for_invalid_day.side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.update_washing_machine_slots(
            day=day,
            washing_machine_id=washing_machine_id,
            time_slots=time_slots
        )

    #Assert
    presenter.raise_exception_for_invalid_day.assert_called_once_with()


def test_update_slots_interactor_raise_invalid_washing_machine_id():
    #Arrange
    day = "Monday"
    washing_machine_id = "wm8"
    time_slots = [
        {
            "start_time" : "06:00",
            "end_time" : "07:00"
        },
        {
            "start_time" : "07:00",
            "end_time" : "08:00"
        },
        {
            "start_time" : "08:00",
            "end_time" : "09:00"
        }
    ]

    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)        
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateWashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    washing_machine_storage.is_valid_washing_machine_id.return_value = False
    presenter.raise_exception_for_invalid_washing_machine_id.side_effect = \
        BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.update_washing_machine_slots(
            day=day,
            washing_machine_id=washing_machine_id,
            time_slots=time_slots
        )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )
    presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once_with()




@patch('slot_booking.interactors.update_washing_machine_slots_interactor.UpdateWashingMachineSlotsInteractor._check_for_invalid_time_slots')

def test_update_slots_interactor_raise_invalid_time_slots(invalid_time_slot_mock):
    #Arrange
    day = "Monday"
    washing_machine_id = "wm8"
    time_slots = [
        {
            "start_time" : "06:00",
            "end_time" : "07:00"
        },
        {
            "start_time" : "06:30",
            "end_time" : "08:00"
        },
        {
            "start_time" : "08:00",
            "end_time" : "09:00"
        }
    ]

    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)        
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateWashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    invalid_time_slot_mock.return_value = True
    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    presenter.raise_exception_for_invalid_time_slots.side_effect = \
        BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.update_washing_machine_slots(
            day=day,
            washing_machine_id=washing_machine_id,
            time_slots=time_slots
        )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )
    presenter.raise_exception_for_invalid_time_slots.assert_called_once_with()


@patch('slot_booking.interactors.update_washing_machine_slots_interactor.UpdateWashingMachineSlotsInteractor._check_for_invalid_time_slots')
def test_update_slots_interactor_returns_updated_response(invalid_time_slot_mock):
    #Arrange
    day = "Monday"
    washing_machine_id = "wm1"
    time_slots = [
        {
            "start_time" : "06:00",
            "end_time" : "07:00"
        },
        {
            "start_time" : "07:00",
            "end_time" : "08:00"
        },
        {
            "start_time" : "08:00",
            "end_time" : "09:00"
        }
    ]
    expected_updated_response = "Successfully Update"

    washing_machine_storage = create_autospec(
        WashingMachineStorageInterface)
    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateWashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    
    washing_machine_storage.is_valid_washing_machine_id.return_value = True
    invalid_time_slot_mock.return_value = False
    presenter.get_response_for_update_time_slots.return_value = \
        expected_updated_response

    #Act
    update_response = interactor.update_washing_machine_slots(day=day,
        washing_machine_id=washing_machine_id, time_slots=time_slots
    )

    #Assert
    washing_machine_storage.is_valid_washing_machine_id.assert_called_once_with(
        washing_machine_id=washing_machine_id
    )

    washing_machine_slot_storage.update_time_slots.assert_called_once()
    presenter.get_response_for_update_time_slots.assert_called_once_with()

    assert update_response == expected_updated_response


'''
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
'''