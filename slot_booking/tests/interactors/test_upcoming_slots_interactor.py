from unittest.mock import create_autospec

from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.upcoming_slots_interactor import \
    UpcomingSlotsInteractor

import pytest

pytestmark = pytest.mark.django_db


def test_get_upcoming_slots_interactor_returns_upcoming_slots(
    upcoming_slots_dtos):
    #Arrange
    user_id = 2
    expected_slots = {
      "upcoming_slots":  [
            {
                "date": "2020-08-10",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm1"
            },
            {
                "date": "2020-08-18",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm2"
            }
        ]
    }

    user_slot_storage = create_autospec(
        UserSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpcomingSlotsInteractor(
        user_slot_storage=user_slot_storage,
        presenter=presenter
    )

    user_slot_storage.get_upcoming_slots.return_value = \
        upcoming_slots_dtos
    presenter.get_response_for_upcoming_slots.return_value = expected_slots

    #Act
    upcoming_slots = interactor.get_upcoming_slots(
        user_id=user_id)

    #Assert

    user_slot_storage.get_upcoming_slots.assert_called_once_with(
        user_id=user_id)
    presenter.get_response_for_upcoming_slots.assert_called_once_with(
        upcoming_slots_dtos)

    assert upcoming_slots == expected_slots



def test_get_upcoming_slots_interactor_returns_upcoming_slots_empty():
    #Arrange
    user_id = 2
    upcoming_slots_dtos = []
    expected_slots = {
      "upcoming_slots":  []
    }

    user_slot_storage = create_autospec(
        UserSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpcomingSlotsInteractor(
        user_slot_storage=user_slot_storage,
        presenter=presenter
    )

    user_slot_storage.get_upcoming_slots.return_value = \
        upcoming_slots_dtos
    presenter.get_response_for_upcoming_slots.return_value = expected_slots

    #Act
    upcoming_slots = interactor.get_upcoming_slots(
        user_id=user_id)

    #Assert

    user_slot_storage.get_upcoming_slots.assert_called_once_with(
        user_id=user_id)
    presenter.get_response_for_upcoming_slots.assert_called_once_with(
        upcoming_slots_dtos)

    assert upcoming_slots == expected_slots
