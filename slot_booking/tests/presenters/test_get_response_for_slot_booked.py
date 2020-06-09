from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_slot_booked():
    #Arrange
    expected_response = "Slot Booked Successfully"

    presenter = PresenterImplementation()

    #Act
    response = presenter.get_response_for_slot_booked()

    #Assert
    assert response == expected_response
