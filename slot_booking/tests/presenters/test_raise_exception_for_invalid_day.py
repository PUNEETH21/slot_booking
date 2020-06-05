from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from slot_booking.constants.exception_messages import \
    INVALID_DAY_EXCEPTION

def test_raise_exception_for_invalid_day():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = \
        "Invalid Day, try with valid Day"
    exception_res_status = "INVALID_DAY"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_invalid_day()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
