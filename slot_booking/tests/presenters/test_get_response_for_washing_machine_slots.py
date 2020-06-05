from slot_booking.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_washing_machine_slots_returns_slots(
    washing_machine_slots_dtos):
    
    #Arrange
    expected_available_slot_dict = {
      "washing_machine_slots":  [
            {
                "start_time": "19:22:46.810366",
                "end_time": "20:22:46.810366",
            },
            {
                "start_time": "20:22:46.810366",
                "end_time": "21:22:46.810366",
            }
        ]
    }

    presenter = PresenterImplementation()

    #Act
    available_slots_dict = presenter.get_response_for_washing_machine_slots(
        washing_machine_slots_dtos=washing_machine_slots_dtos)

    #Assert
    assert available_slots_dict == expected_available_slot_dict

def test_get_response_for_washing_machine_slots_returns_slots_empty():
    
    #Arrange
    washing_machine_slots_dtos = []
    expected_available_slot_dict = {"washing_machine_slots": []}

    presenter = PresenterImplementation()

    #Act
    available_slots_dict = presenter.get_response_for_washing_machine_slots(
        washing_machine_slots_dtos=washing_machine_slots_dtos)

    #Assert
    assert available_slots_dict == expected_available_slot_dict
