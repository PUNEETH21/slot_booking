from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_previous_slots_returns_previous_slots_empty(
    previous_slots_dtos):

    #Arrange
    previous_slots_dtos = []
    expected_previous_slots = {
      "previous_slots":  []
    }

    presenter = PresenterImplementation()

    #Act
    previous_slots = presenter.get_response_for_previous_slots(
        previous_slots_dtos=previous_slots_dtos)

    #Assert
    assert previous_slots == expected_previous_slots

