from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_upcoming_slots_returns_upcoming_slots(
    upcoming_slots_dtos):

    #Arrange
    expected_upcoming_slots = {
      "upcoming_slots":  [
            {
                "date": "2021-07-15",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm1"
            },
            {
                "date": "2021-08-24",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm2"
            }
        ]
    }

    presenter = PresenterImplementation()

    #Act
    upcoming_slots = presenter.get_response_for_upcoming_slots(
        upcoming_slots_dtos=upcoming_slots_dtos)

    #Assert
    assert upcoming_slots == expected_upcoming_slots

def test_get_response_for_upcoming_slots_returns_upcoming_slots_empty():

    #Arrange
    upcoming_slots_dtos = []
    expected_upcoming_slots = {
      "upcoming_slots":  []
    }

    presenter = PresenterImplementation()

    #Act
    upcoming_slots = presenter.get_response_for_upcoming_slots(
        upcoming_slots_dtos=upcoming_slots_dtos)

    #Assert
    assert upcoming_slots == expected_upcoming_slots
