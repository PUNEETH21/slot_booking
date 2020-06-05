from slot_booking.storages.washing_machine_slot_storage_implementation import \
    WashingMachineSlotStorageImplementation
import pytest
from slot_booking.dtos.dtos import TimeSlotDto
from datetime import datetime, time

@pytest.mark.django_db
def test_get_washing_machine_slots(washing_machine_slot):
    #Arrange
    washing_machine_id = "wm1"
    day = "Monday"
    storage = WashingMachineSlotStorageImplementation()
    expected_output = [
        TimeSlotDto(start_time="05:00:00", end_time="06:00:00"),
        TimeSlotDto(start_time="06:00:00", end_time="07:00:00"),
        TimeSlotDto(start_time="07:00:00", end_time="08:00:00")
    ]

    #Act
    response = storage.get_washing_machine_slots(day=day,
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert response == expected_output

@pytest.mark.django_db
def test_get_washing_machine_slots_empty(washing_machine_slot):
    #Arrange
    washing_machine_id = "wm4"
    day = "Monday"
    storage = WashingMachineSlotStorageImplementation()
    expected_output = []

    #Act
    response = storage.get_washing_machine_slots(day=day,
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert response == expected_output
