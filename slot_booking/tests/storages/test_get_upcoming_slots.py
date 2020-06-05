from slot_booking.storages.user_slot_storage_implementation import \
    UserSlotStorageImplementation
import pytest
from slot_booking.dtos.dtos import UpcomingSlotDto
from datetime import datetime, time

@pytest.mark.django_db
def test_get_upcoming_slots_return_upcoming_slots_dto(user_slot):
    #Arrange
    user_id = 1
    storage = UserSlotStorageImplementation()
    expected_slots = [
        UpcomingSlotDto(date="2030-05-14", start_time="05:00:00", 
        end_time="06:00:00", washing_machine_id="wm1"),
        UpcomingSlotDto(date="2030-05-20", start_time="05:00:00", 
        end_time="06:00:00", washing_machine_id="wm1"),
        UpcomingSlotDto(date="2030-05-26", start_time="07:00:00", 
        end_time="08:00:00", washing_machine_id="wm2")
    ]

    #Act
    upcoming_slots = storage.get_upcoming_slots(user_id=user_id)

    #Assert
    assert upcoming_slots == expected_slots

@pytest.mark.django_db
def test_get_upcoming_slots_return_upcoming_slots_dto_empty(user_slot):
    #Arrange
    user_id = 2
    storage = UserSlotStorageImplementation()
    expected_slots = []

    #Act
    upcoming_slots = storage.get_upcoming_slots(user_id=user_id)

    #Assert
    assert upcoming_slots == expected_slots
