from slot_booking.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_available_slots_returns_slots(available_slots_dtos):
    
    #Arrange
    expected_available_slots_response = {
        "available_slots": [
            {
                "date": "2020-06-04",
                "time_slots": [
                    {
                        "start_time" : "06:00:00",
                        "end_time" : "07:00:00",
                        "is_available": True
                    },
                    {
                        "start_time" : "07:00:00",
                        "end_time" : "08:00:00",
                        "is_available" : False
                    }
                ]
            },
            {
                "date": "2020-06-05",
                "time_slots": [
                    {
                        "start_time" : "06:30:00",
                        "end_time" : "07:30:00",
                        "is_available": True
                    },
                    {
                        "start_time" : "07:30:00",
                        "end_time" : "08:30:00",
                        "is_available" : False
                    }
                ]
            }
        ]
    }



    presenter = PresenterImplementation()

    #Act
    available_slots_response = presenter.get_response_for_available_slots(
        available_slots_dtos=available_slots_dtos)

    #Assert
    assert available_slots_response == expected_available_slots_response

from slot_booking.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_available_slots_returns_empty():
    
    #Arrange
    available_slots_dtos = []
    expected_available_slots_response = {
        "available_slots": []
    }

    presenter = PresenterImplementation()

    #Act
    available_slots_response = presenter.get_response_for_available_slots(
        available_slots_dtos=available_slots_dtos)

    #Assert
    assert available_slots_response == expected_available_slots_response

