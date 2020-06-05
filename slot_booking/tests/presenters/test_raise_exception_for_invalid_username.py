from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from slot_booking.constants.exception_messages import \
    INVALID_USERNAME_EXCEPTION

def test_raise_exception_for_invalid_username():
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
