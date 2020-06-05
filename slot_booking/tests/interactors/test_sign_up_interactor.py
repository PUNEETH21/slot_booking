from unittest.mock import create_autospec

from slot_booking.interactors.storages.user_storage_interface import \
    UserStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.interactors.sign_up_interactor import SignUpInteractor

from slot_booking.exceptions.exceptions import InvalidUsername

from django_swagger_utils.drf_server.exceptions import BadRequest
import pytest


pytestmark = pytest.mark.django_db


def test_sign_up_invalid_username_raise_exceptions():
    #Arrange
    username = "username"
    password = "password"

    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_username.return_value = True
    presenter.raise_exception_for_invalid_username.side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.sign_up(
            username=username,
            password=password
        )

    #Assert

    storage.is_valid_username.assert_called_once_with(username=username)
    presenter.raise_exception_for_invalid_username.assert_called_once_with()

def test_sign_up_return_user_created_response():
    #Arrange
    username = "username1"
    password = "password"
    expected_sign_up_response = "User Created Successfully"

    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_username.return_value = False
    presenter.get_response_for_sign_up.return_value = expected_sign_up_response

    #Act
    sign_up_response = interactor.sign_up(username=username, 
        password=password)

    #Assert

    storage.is_valid_username.assert_called_once_with(username=username)
    storage.create_user.assert_called_once_with(
        username=username, password=password
    )
    presenter.get_response_for_sign_up.assert_called_once_with()
    assert sign_up_response == expected_sign_up_response





'''
def test_empty_username_raise_exceptions():
    #Arrange
    username = ""
    password = "password",
    confirm_password = "password"
    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter
        )

    presenter.raise_exception_for_empty_username.side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.sign_up(
            username=username,
            password=password,
            confirm_password=confirm_password
        )

    #Assert

    presenter.raise_exception_for_empty_username.assert_called_once_with()

def test_empty_password_raise_exceptions():
    #Arrange
    username = "username"
    password = ""
    confirm_password = "password"
    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter
        )

    presenter.raise_exception_for_empty_password.side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.sign_up(
            username=username,
            password=password,
            confirm_password=confirm_password
        )

    #Assert

    presenter.raise_exception_for_empty_password.assert_called_once_with()

def test_password_not_confirmed_raise_exceptions():
    #Arrange
    username = "username"
    password = "pow"
    confirm_password = "password"
    storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter
        )

    presenter.raise_exception_for_password_not_confirmed.side_effect=BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.sign_up(
            username=username,
            password=password,
            confirm_password=confirm_password
        )

    #Assert

    presenter.raise_exception_for_password_not_confirmed.assert_called_once_with()
'''