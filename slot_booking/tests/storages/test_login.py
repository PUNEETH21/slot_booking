from slot_booking.storages.user_storage_implementation import \
    UserStorageImplementation
import pytest
from slot_booking.dtos.dtos import TimeSlotDto
from datetime import datetime, time
from slot_booking.models.user import User

@pytest.mark.django_db
def test_login_invalid_username_return_true(user):
    #Arrange
    username = "username"
    expected_bool = True
    storage = UserStorageImplementation()

    #Act
    actual_bool = storage.is_valid_username(username=username)

    #Assert
    assert actual_bool == expected_bool

@pytest.mark.django_db
def test_login_invalid_username_return_false(user):
    #Arrange
    username = "user"
    expected_bool = False
    storage = UserStorageImplementation()

    #Act
    actual_bool = storage.is_valid_username(username=username)

    #Assert
    assert actual_bool == expected_bool

@pytest.mark.django_db
def test_login_invalid_password_return_true(user):
    #Arrange
    password = "password"
    expected_bool = True
    storage = UserStorageImplementation()

    #Act
    actual_bool = storage.is_valid_password(password=password)

    #Assert
    assert actual_bool == expected_bool

@pytest.mark.django_db
def test_login_invalid_password_return_false(user):
    #Arrange
    password = "pass"
    expected_bool = False
    storage = UserStorageImplementation()

    #Act
    actual_bool = storage.is_valid_password(password=password)

    #Assert
    assert actual_bool == expected_bool

@pytest.mark.django_db
def test_login_invalid_username_password_return_user_id(user):
    #Arrange
    username = "username"
    password = "password"
    user_obj = User.objects.get(username=username, password=password)
    expected_user_id = user_obj
    storage = UserStorageImplementation()

    #Act
    actual_user_id = storage.is_valid_username_password(
        username=username,
        password=password
    )

    #Assert
    assert actual_user_id == expected_user_id

@pytest.mark.django_db
def test_login_invalid_username_password_return_none(user):
    #Arrange
    username = "username"
    password = "password1"
    expected_user_id = None
    storage = UserStorageImplementation()

    #Act
    actual_user_id = storage.is_valid_username_password(
        username=username,
        password=password
    )

    #Assert
    assert actual_user_id == expected_user_id
