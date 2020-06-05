from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

def test_get_response_for_previous_slots_returns_previous_slots(
    previous_slots_dtos):

    #Arrange
    expected_previous_slots = {
      "previous_slots":  [
            {
                "date": "29-05-2020",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm1"
            },
            {
                "date": "23-05-2020",
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
                "washing_machine_id": "wm2"
            }
        ]
    }

    presenter = PresenterImplementation()

    #Act
    previous_slots = presenter.get_response_for_previous_slots(
        previous_slots_dtos=previous_slots_dtos)

    #Assert
    assert previous_slots == expected_previous_slots

