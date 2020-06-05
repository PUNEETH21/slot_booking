from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_get_washing_machine_details(
    washing_machine_details_dto):
    #Arrange
    expected_response = {
        "washing_machine_id" : "wm1",
        "is_active" : True
    }

    presenter = PresenterImplementation()

    #Act
    response = presenter.get_response_for_get_washing_machine_details(
        washing_machine_details_dto)

    #Assert
    assert response == expected_response
