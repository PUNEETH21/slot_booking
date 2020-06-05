from unittest.mock import create_autospec

from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface
from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.storages.configure_slot_storage_interface \
    import ConfigureSlotStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from datetime import datetime, timedelta

from slot_booking.dtos.dtos import AvailableTimeSlotDto

from slot_booking.interactors.available_slots_interactor import \
    AvailableSlotsInteractor


import pytest
#from slot_booking.tests.interactors.conftest import available_slots_dtos
#from slot_booking.dtos.dtos import AvailableSlotsDto
from unittest.mock import patch

pytestmark = pytest.mark.django_db

@patch('slot_booking.interactors.available_slots_interactor.AvailableSlotsInteractor._configure_days_to_book')

def test_get_available_slots_interactor_return_empty(configure_days_to_book_mock):
    #Arrange
    user_id = 1
    configure_days_to_book_mock.return_value = 0
    expected_available_slots_response = {
        "available_slots": []
    }


    user_slot_storage = create_autospec(UserSlotStorageInterface)
    configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = AvailableSlotsInteractor(
        user_slot_storage = user_slot_storage,
        configure_slot_storage = configure_slot_storage,
        washing_machine_slot_storage = washing_machine_slot_storage,
        presenter=presenter
    )

    presenter.get_response_for_available_slots.return_value = \
        expected_available_slots_response
    available_slots_dtos = []

    #Act
    available_slots_response = interactor.available_slots(user_id)

    #Assert
    presenter.get_response_for_available_slots.assert_called_once_with(
        available_slots_dtos)


'''

@patch('slot_booking.interactors.available_slots_interactor.AvailableSlotsInteractor._configure_days_to_book')

def test_get_available_slots_interactor(configure_days_to_book_mock):
    #Arrange
    user_id = 1
    configure_days_to_book_mock.return_value = 0
    expected_available_slots_response = {
        "available_slots": [
            {
                "date": "2020-06-04",
                "time_slots": [
                    {
                        "start_time" : "06:00",
                        "end_time" : "07:00",
                        "is_available": True
                    },
                    {
                        "start_time" : "07:00",
                        "end_time" : "08:00",
                        "is_available" : False
                    },
                    {
                        "start_time" : "08:00",
                        "end_time" : "09:00",
                        "is_available" : True
                    }
                ]
            }
        ]
    }


    user_slot_storage = create_autospec(UserSlotStorageInterface)
    configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
    washing_machine_slot_storage = create_autospec(
        WashingMachineSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = AvailableSlotsInteractor(
        user_slot_storage = user_slot_storage,
        configure_slot_storage = configure_slot_storage,
        washing_machine_slot_storage = washing_machine_slot_storage,
        presenter=presenter
    )

    presenter.get_response_for_available_slots_empty.return_value = \
        expected_response

    #Act
    available_slots_response = interactor.available_slots(user_id)

    #Assert
    presenter.get_response_for_available_slots_empty.assert_called_once_with()



@patch('slot_booking.interactors.available_slots_interactor.AvailableSlotsInteractor._configure_days_to_book')

def test_get_available_slots_interactor(configure_days_to_book_mock):
    #Arrange
    configure_days_to_book_mock.return_value = 0
    expected_output = {
        "avaliable_slots": [
            {
              "date": "2020-05-28",
              "time_slots": [
                {
                  "from_time": "19:22:46.810366",
                  "to_time": "20:22:46.810366",
                  "is_available": True
                }
              ]
            },
            {
              "date": "2020-05-28",
              "time_slots": [
                {
                  "from_time": "20:22:46.810366",
                  "to_time": "21:22:46.810366",
                  "is_available": False
                }
              ]
            }
        ]
    }

    Available_Slots_Dto = AvailableSlotsDto(
        avaliable_slots_dto=available_slots_dtos
    )
    storage = create_autospec(AvailableSlotsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AvailableSlotsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.get_available_slots.return_value = available_slots_dtos
    presenter.get_available_slots_response.return_value = expected_output

    #Act
    available_slots = interactor.available_slots()

    #Assert
    storage.get_available_slots.assert_called_once_with()
    presenter.get_available_slots_response.assert_called_once_with(
        available_slots_dtos)
    assert available_slots == expected_output




'''