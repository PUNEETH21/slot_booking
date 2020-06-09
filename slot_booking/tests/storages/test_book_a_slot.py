from slot_booking.storages.washing_machine_slot_storage_implementation \
    import WashingMachineSlotStorageImplementation
from slot_booking.storages.user_slot_storage_implementation \
    import UserSlotStorageImplementation
import pytest
from slot_booking.dtos.dtos import WashingMachineDto
from datetime import datetime, time

@pytest.mark.django_db
def test_book_a_slot_washing_machines_in_given_slot_return_washing_machine_ids(
    washing_machine_slot):
    #Arrange
    day = "Monday"
    start_time = "05:00:00"
    end_time = "06:00:00"
    expected_washing_machine_ids = ["wm1", "wm2", "wm3"]
    storage = WashingMachineSlotStorageImplementation()

    #Act
    washing_machine_ids = storage.washing_machines_in_given_slot(
        day=day, start_time=start_time, end_time=end_time
    )

    #Assert
    assert washing_machine_ids == expected_washing_machine_ids

@pytest.mark.django_db
def test_book_a_slot_create_user_slot_return_true(
    user, user_slot):
    user_id=2
    date = "2020-05-14"
    start_time = "05:00:00"
    end_time = "06:00:00"
    washing_machine_ids = ["wm1", "wm2", "wm3"]
    expected_create_user_slot_response = True
    storage = UserSlotStorageImplementation()

    #Act
    create_user_slot_response = storage.create_user_slot(user_id=user_id, date=date, start_time=start_time, 
        end_time=end_time, washing_machines_ids=washing_machine_ids
    )

    #Assert
    assert create_user_slot_response == expected_create_user_slot_response


@pytest.mark.django_db
def test_book_a_slot_create_user_slot_return_false(
    user, user_slot):
    user_id=2
    date = "2020-05-14"
    start_time = "05:00:00"
    end_time = "06:00:00"
    washing_machine_ids = ["wm1"]
    expected_create_user_slot_response = False
    storage = UserSlotStorageImplementation()

    #Act
    create_user_slot_response = storage.create_user_slot(user_id=user_id, date=date, start_time=start_time, 
        end_time=end_time, washing_machines_ids=washing_machine_ids
    )

    #Assert
    assert create_user_slot_response == expected_create_user_slot_response
