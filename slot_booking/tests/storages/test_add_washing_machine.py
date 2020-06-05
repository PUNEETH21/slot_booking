from slot_booking.storages.washing_machine_storage_implementation import \
    WashingMachineStorageImplementation

from slot_booking.models.washing_machine import Washingmachine

import pytest
@pytest.mark.django_db
def test_add_washing_machine_is_valid_machine_id_return_true(washing_machine):
    #Arrange
    washing_machine_id = "wm1"
    storage = WashingMachineStorageImplementation()
    expected_boolean = True

    #Act
    actual_boolean = storage.is_valid_washing_machine_id(
        washing_machine_id=washing_machine_id
    )

    #Assert
    assert actual_boolean == expected_boolean

@pytest.mark.django_db
def test_add_washing_machine_is_valid_machine_id_return_false(washing_machine):
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
def test_add_washing_machine_status_true():
    #Arrange
    washing_machine_id = "wm1"
    is_active = True
    storage = WashingMachineStorageImplementation()
    expected_washing_machine_id = "wm1"
    expected_washing_machine_status = True
    
    #Act
    storage.add_washing_machine(
        washing_machine_id=washing_machine_id, is_active=is_active
    )

    washing_machine_obj = Washingmachine.objects.get(
        washing_machine_id=washing_machine_id, is_active=is_active
    )

    #Assert
    assert expected_washing_machine_id == \
        washing_machine_obj.washing_machine_id
    assert expected_washing_machine_status == washing_machine_obj.is_active


@pytest.mark.django_db
def test_add_washing_machine_status_false():
    #Arrange
    washing_machine_id = "wm8"
    is_active = False
    storage = WashingMachineStorageImplementation()
    expected_washing_machine_id = "wm8"
    expected_washing_machine_status = False

    #Act
    storage.add_washing_machine(
        washing_machine_id=washing_machine_id, is_active=is_active
    )

    washing_machine_obj = Washingmachine.objects.get(
        washing_machine_id=washing_machine_id, is_active=is_active
    )

    #Assert
    assert expected_washing_machine_id == \
        washing_machine_obj.washing_machine_id
    assert expected_washing_machine_status == washing_machine_obj.is_active

