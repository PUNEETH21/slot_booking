import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.constants.exception_messages import (
    INVALID_USERNAME_EXCEPTION, INVALID_PASSWORD_EXCEPTION,
    INVALID_USERNAME_PASSWORD_EXCEPTION
)

def test_login_raise_exception_for_invalid_username():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = "Invalid Username, try with valid Username"
    exception_res_status = "INVALID_USERNAME"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_invalid_username()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

def test_login_raise_exception_for_invalid_password():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = "Invalid Password, try with valid Password"
    exception_res_status = "INVALID_PASSWORD"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_invalid_password()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

def test_login_raise_exception_for_invalid_username_password():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = "Invalid Username Password, try with valid Username Password"
    exception_res_status = "INVALID_USERNAME_PASSWORD"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_invalid_username_password()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

pytestmark = pytest.mark.django_db
def test_get_response_for_login(user_auth_tokens_dto):
    #Arrange
    expected_response = {
        "is_admin" : True,
        "access_token" : 'edsas34t43w',
        "refresh_token" : 'adsfalfj343',
        "expires_in" : "2020-05-31 16:29:22.751566"
    }

    presenter = PresenterImplementation()

    #Act
    actual_response = presenter.get_response_for_login(
        token_details_dto=user_auth_tokens_dto)

    #Assert
    assert actual_response == expected_response
