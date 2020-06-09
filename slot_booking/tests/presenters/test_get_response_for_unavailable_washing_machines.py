from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_unavailable_washing_machines():
    #Arrange
    expected_response = "Unavailable Washing Machines Slot Not Booked"

    presenter = PresenterImplementation()

    #Act
    response = presenter.get_response_for_unavailable_washing_machines()

    #Assert
    assert response == expected_response
