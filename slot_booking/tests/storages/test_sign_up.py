from slot_booking.storages.user_storage_implementation import \
    UserStorageImplementation
from slot_booking.models.user import User

import pytest

@pytest.mark.django_db
def test_sign_up_create_user(user):
    #Arrange
    username = "USER"
    password = "WORD"
    storage = UserStorageImplementation()

    #Act
    storage.create_user(username=username, password=password)
    user_obj = User.objects.get(username=username, password=password)
    created_user_name = user_obj.username
    created_password = user_obj.password

    #Assert
    assert created_user_name == username
    assert created_password == password

