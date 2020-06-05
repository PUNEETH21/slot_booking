from slot_booking.storages.washing_machine_slot_storage_implementation import \
    WashingMachineSlotStorageImplementation

from slot_booking.dtos.dtos import WashingMachineDetailsDto
import pytest
from slot_booking.models.washing_machine_slot import WashingmachineSlot

@pytest.mark.django_db
def test_get_washing_machine_details_is_valid_machine_id_return_true(
    washing_machine_slot, time_slots_dtos):
    #Arrange
    day = "Thursday"
    washing_machine_id = "wm1"
    time_slots = [
        {
            "start_time" : "06:30",
            "end_time" : "07:30"
        },
        {
            "start_time" : "07:30",
            "end_time" : "08:30"
        },
        {
            "start_time" : "08:30",
            "end_time" : "09:30"
        }
    ]

    storage = WashingMachineSlotStorageImplementation()
    expected_boolean = True

    #Act
    storage.update_time_slots(
        time_slots_dtos = time_slots_dtos
    )

    wm_objs = WashingmachineSlot.objects.filter(
        day=day, washing_machine_id=washing_machine_id)
    
    start_time1 = str(wm_objs[0].start_time)
    start_time2 = str(wm_objs[1].start_time)
    start_time3 = str(wm_objs[2].start_time)
    end_time1 = str(wm_objs[0].end_time)
    end_time2 = str(wm_objs[1].end_time)
    end_time3 = str(wm_objs[2].end_time)
    expected_start_time1= "06:30:00"
    expected_start_time2= "07:30:00"
    expected_start_time3= "08:30:00"
    expected_end_time1 = "07:30:00"
    expected_end_time2 = "08:30:00"
    expected_end_time3 = "09:30:00"

    #Assert
    assert start_time1 == expected_start_time1
    assert start_time2 == expected_start_time2
    assert start_time3 == expected_start_time3
    assert end_time1 == expected_end_time1
    assert end_time2 == expected_end_time2
    assert end_time3 == expected_end_time3

'''
@pytest.mark.django_db
def test_get_washing_machine_details_is_valid_machine_id_return_false(
    washing_machine):
    #Arrange
    washing_machine_id = "wm19"
    storage = WashingMachineStorageImplementation()
    expected_boolean = False

    #Act
    actual_boolean = storage.is_valid_washing_machine_id(
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert actual_boolean == expected_boolean

@pytest.mark.django_db
def test_get_washing_machine_details_status_true(
    washing_machine_details_dto_status_true):

    #Arrange
    washing_machine_id = "wm5"
    storage = WashingMachineStorageImplementation()
    expected_details_dto = WashingMachineDetailsDto(
        washing_machine_id="wm5", is_active=True
    )

    #Act
    details_dto = storage.get_washing_machine_details(
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert details_dto == expected_details_dto

@pytest.mark.django_db
def test_get_washing_machine_details_status_false(
    washing_machine_details_dto_status_false):

    #Arrange
    washing_machine_id = "wm6"
    storage = WashingMachineStorageImplementation()
    expected_details_dto = WashingMachineDetailsDto(
        washing_machine_id="wm6", is_active=False
    )

    #Act
    details_dto = storage.get_washing_machine_details(
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert details_dto == expected_details_dto
'''