from unittest.mock import create_autospec

from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface

from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.previous_slots_interactor import \
    PreviousSlotsInteractor

import pytest

pytestmark = pytest.mark.django_db


def test_get_previous_slots_interactor_returns_previous_slots(
    previous_slots_dtos):
    #Arrange
    user_id = 2
    expected_slots = {
      "previous_slots":  [
            {
                "date": "29-05-2020",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm1"
            },
            {
                "date": "23-05-2020",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm2"
            }
        ]
    }

    user_slot_storage = create_autospec(
        UserSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = PreviousSlotsInteractor(
        user_slot_storage=user_slot_storage,
        presenter=presenter
    )

    user_slot_storage.get_previous_slots.return_value = \
        previous_slots_dtos
    presenter.get_response_for_previous_slots.return_value = expected_slots

    #Act
    previous_slots = interactor.get_previous_slots(
        user_id=user_id)

    #Assert

    user_slot_storage.get_previous_slots.assert_called_once_with(
        user_id=user_id)
    presenter.get_response_for_previous_slots.assert_called_once_with(
        previous_slots_dtos)
    assert previous_slots == expected_slots

def test_get_previous_slots_interactor_returns_empty_previous_slots(
    ):
    #Arrange
    user_id = 2
    previous_slots_dtos = []
    expected_slots = {
      "previous_slots":  []
    }

    user_slot_storage = create_autospec(
        UserSlotStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = PreviousSlotsInteractor(
        user_slot_storage=user_slot_storage,
        presenter=presenter
    )

    user_slot_storage.get_previous_slots.return_value = \
        previous_slots_dtos
    presenter.get_response_for_previous_slots.return_value = expected_slots

    #Act
    previous_slots = interactor.get_previous_slots(
        user_id=user_id)

    #Assert

    user_slot_storage.get_previous_slots.assert_called_once_with(
        user_id=user_id)
    presenter.get_response_for_previous_slots.assert_called_once_with(
        previous_slots_dtos)
    assert previous_slots == expected_slots

