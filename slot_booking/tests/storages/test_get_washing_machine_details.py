from slot_booking.storages.washing_machine_storage_implementation import \
    WashingMachineStorageImplementation

from slot_booking.dtos.dtos import WashingMachineDetailsDto
import pytest

@pytest.mark.django_db
def test_get_washing_machine_details_is_valid_machine_id_return_true(
    washing_machine):
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
