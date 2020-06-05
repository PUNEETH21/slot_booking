from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_add_washing_machine():
    #Arrange
    expected_response = "Washing Machine Added Successfully"

    presenter = PresenterImplementation()

    #Act
    response = presenter.get_response_for_add_washing_machine()

    #Assert
    assert response == expected_response
