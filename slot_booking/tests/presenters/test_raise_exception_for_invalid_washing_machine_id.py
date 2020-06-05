from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from slot_booking.constants.exception_messages import \
    INVALID_WASHING_MACHINE_ID_EXCEPTION

def test_raise_exception_for_washing_machine_id():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = \
        "Invalid Washing Machine Id, try with valid Washing Machine Id"
    exception_res_status = "INVALID_WASHING_MACHINE_ID"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_invalid_washing_machine_id()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
