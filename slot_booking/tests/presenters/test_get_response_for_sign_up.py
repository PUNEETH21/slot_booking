from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_sign_up():
    #Arrange
    expected_sign_up_response = "User Created Successfully"

    presenter = PresenterImplementation()

    #Act
    sign_up_response = presenter.get_response_for_sign_up()

    #Assert
    assert sign_up_response == expected_sign_up_response
