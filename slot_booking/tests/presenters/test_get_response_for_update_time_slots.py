from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_update_time_slots(
    washing_machine_details_dto):
    #Arrange
    expected_update_response = "Successfully Update The Washing Machine Slots"

    presenter = PresenterImplementation()

    #Act
    update_response = presenter.get_response_for_update_time_slots()

    #Assert
    assert update_response == expected_update_response
