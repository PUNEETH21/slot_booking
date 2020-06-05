from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from slot_booking.constants.exception_messages import \
    WASHING_MACHINE_ID_ALREADY_EXIST_EXCEPTION

def test_raise_exception_for_washing_machine_id_already_exist():
    #Arrange
    json_presenter = PresenterImplementation()
    exception_message = "Washing Machine Id Already Exist, try with another washing_machine_id"
    exception_res_status = "WASHING_MACHINE_ID_ALREADY_EXIST"

    #Act
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_exception_for_washing_machine_id_already_exist()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
