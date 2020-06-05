from slot_booking.storages.washing_machine_slot_storage_implementation import \
    WashingMachineSlotStorageImplementation
from slot_booking.interactors.storages.configure_slot_storage_interface \
    import ConfigureSlotStorageInterface
from slot_booking.storages.user_slot_storage_implementation \
    import UserSlotStorageImplementation

import pytest
from slot_booking.dtos.dtos import TimeSlotDto, TimeRangeCountDto
from datetime import datetime, time

@pytest.mark.django_db
def test_available_slots_get_day_slots(washing_machine_slot):
    #Arrange
    day = "Monday"
    storage = WashingMachineSlotStorageImplementation()
    expected_day_response = [
        TimeRangeCountDto(start_time='05:00:00', end_time='06:00:00', count=3),
        TimeRangeCountDto(start_time='06:00:00', end_time='07:00:00', count=1),
        TimeRangeCountDto(start_time='07:00:00', end_time='08:00:00', count=2)
    ]

    #Act
    day_response = storage.get_day_slots(day=day)

    #Assert
    assert day_response == expected_day_response

@pytest.mark.django_db
def test_available_slots_get_date_slots(user_slot):
    #Arrange
    date = "2020-05-20"
    storage = UserSlotStorageImplementation()
    expected_date_response = [
        TimeRangeCountDto(start_time='05:00:00', end_time='06:00:00', count=2),
        TimeRangeCountDto(start_time='06:00:00', end_time='07:00:00', count=1)
    ]

    #Act
    date_response = storage.get_date_slots(date=date)

    #Assert
    assert date_response == expected_date_response


'''
@pytest.mark.django_db
def test_get_alloted_slots_empty(washing_machine_slot):
    #Arrange
    washing_machine_id = "wm4"
    day = "Monday"
    storage = WashingMachineSlotStorageImplementation()
    expected_output = []

    #Act
    response = storage.get_alloted_slots(day=day,
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert response == expected_output
'''