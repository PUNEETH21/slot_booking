from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from slot_booking.constants.exception_messages import \
    INVALID_DATE_EXCEPTION

def test_raise_exception_for_invalid_date():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = \
        "Invalid Date, try with valid Date"
    exception_res_status = "INVALID_DATE"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_invalid_date()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
