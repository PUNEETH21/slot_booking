from unittest.mock import create_autospec

from slot_booking.storages.user_storage_implementation import \
    UserStorageImplementation
from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

from slot_booking.interactors.login_interactor import LogInInteractor
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common import oauth_user_auth_tokens_service

from unittest.mock import patch

from slot_booking.exceptions.exceptions import InvalidUsername, \
    InvalidPassword, InvalidUsernamePassword

from django_swagger_utils.drf_server.exceptions import NotFound
import pytest

from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from slot_booking.dtos.dtos import UserAuthTokensDto

pytestmark = pytest.mark.django_db

@patch('common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens')
def test_get_access_token(create_user_auth_tokens_mock):
    #Arrange
    username = "username"
    password = "password"
    expected_dto = UserAuthTokensDto(
        user_id 
        access_token = 'edsas34t43w',
        refresh_token = 'adsfalfj343',
        expires_in = "2020-05-24",
    )
    expected_response = {
        "access_token" : 'edsas34t43w',
        "refresh_token" : 'adsfalfj343',
        "expiry_time" : "2020-05-24",
        "is_admin" : True
    }
    create_user_auth_tokens_mock.return_value = expected_dto
    storage = create_autospec(UserStorageImplementation())
    oauth2_storage = create_autospec(OAuth2SQLStorage())
    presenter = create_autospec(PresenterImplementation())
    interactor = LogInInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    storage.is_valid_username.return_value = True
    storage.is_valid_password.return_value = True
    storage.is_valid_username_password.return_value = None
    presenter.get_response_for_login.return_value = expected_response

    #Act
    response = interactor.login(
        username=username,
        password=password
    )

    #Assert
    assert response == expected_response

'''
def test_login_interactor_return_token_details(create_user_auth_tokens_mock):
    #Arrange
    username = "username"
    password = "password"
    expected_response = {
        "access_token" : 'edsas34t43w',
        "refresh_token" : 'adsfalfj343',
        "expiry_time" : "2020-05-24",
        "is_admin" : True
    }
    create_user_auth_tokens_mock.return_value = expected_dto
    storage = create_autospec(UserStorageImplementation())
    oauth2_storage = create_autospec(OAuth2SQLStorage())
    presenter = create_autospec(PresenterImplementation())
    interactor = LogInInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    storage.is_valid_username.return_value = True
    storage.is_valid_password.return_value = True
    storage.is_valid_username_password.return_value = None
    presenter.get_response_for_login.return_value = expected_response

    #Act
    response = interactor.login(
        username=username,
        password=password
    )

    #Assert
    assert response == expected_response
'''

def test_invalid_username_raise_exceptions():
    #Arrange
    username = "user"
    password = "password"

    storage = create_autospec(UserStorageImplementation())
    oauth2_storage = OAuth2SQLStorage()
    presenter = create_autospec(PresenterImplementation())
    interactor = LogInInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )

    storage.is_valid_username.return_value = False
    presenter.raise_exception_for_invalid_username.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
            )

    #Assert

    storage.is_valid_username.assert_called_once_with(username=username)
    presenter.raise_exception_for_invalid_username.assert_called_once_with()

def test_invalid_password_raise_exceptions():
    #Arrange
    username = "user"
    password = "passwd"

    storage = create_autospec(UserStorageImplementation())
    oauth2_storage = OAuth2SQLStorage()
    presenter = create_autospec(PresenterImplementation())
    interactor = LogInInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )

    storage.is_valid_password.return_value = False
    presenter.raise_exception_for_invalid_password.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
            )

    #Assert
    storage.is_valid_password.assert_called_once_with(password=password)
    presenter.raise_exception_for_invalid_password.assert_called_once_with()


def test_invalid_username_and_password_raise_exceptions():
    #Arrange
    username = "user"
    password = "passwd"

    storage = create_autospec(UserStorageImplementation())
    oauth2_storage = OAuth2SQLStorage()
    presenter = create_autospec(PresenterImplementation())
    interactor = LogInInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )

    storage.is_valid_username_password.return_value = False
    presenter.raise_exception_for_invalid_username_password.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
            )

    #Assert
    storage.is_valid_username_password.assert_called_once_with(
        username=username,
        password=password
    )
    presenter.raise_exception_for_invalid_username_password.assert_called_once_with()

