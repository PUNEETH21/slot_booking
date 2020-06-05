# from unittest.mock import create_autospec
# from datetime import datetime
# from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
#     import WashingMachineSlotStorageInterface

# from slot_booking.interactors.storages.user_slot_storage_interface \
#     import UserSlotStorageInterface
# from slot_booking.interactors.storages.configure_slot_storage_interface \
#     import ConfigureSlotStorageInterface

# from slot_booking.interactors.presenters.presenter_interface import \
#     PresenterInterface

# from slot_booking.interactors.book_a_slot_interactor import \
#     BookASlotInteractor

# from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
# import pytest
# import calendar 
# from freezegun import freeze_time
# import unittest
# import mock
# from unittest.mock import patch

# @freeze_time("2020-09-14")
# #@mock.patch('datetime.datetime', return_value=datetime.datetime(2021, 1, 1))
# def test_book_a_slot_raises_exception_for_invalid_date():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     mock_date = '2020-04-01'
#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )
#     presenter.raise_exception_for_invalid_date.side_effect=BadRequest

#     #Act
#     with pytest.raises(BadRequest):
#         interactor.book_a_slot(
#             user_id=user_id, date=mock_date, start_time=start_time, 
#             end_time=end_time
#         )

#     #Assert
#     presenter.raise_exception_for_invalid_date.assert_called_once_with()


# def test_book_a_slot_raises_exception_for_cannot_book_in_date():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     mock_date = '2020-06-30'
#     book_days_after = 8
#     present_date = str(datetime.now().date())
#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )
#     configure_slot_storage.book_days_after.return_value = 8
#     user_slot_storage.cannot_book_in_date.return_value=True
#     presenter.raise_exception_for_cannot_book_in_date.side_effect=BadRequest

#     #Act
#     with pytest.raises(BadRequest):
#         interactor.book_a_slot(
#             user_id=user_id, date=mock_date, start_time=start_time, 
#             end_time=end_time
#         )

#     #Assert
#     user_slot_storage.cannot_book_in_date.assert_called_once_with(
#         user_id, present_date, book_days_after)
#     presenter.raise_exception_for_cannot_book_in_date.assert_called_once_with()


# @freeze_time("2020-06-01")
# def test_book_a_slot_return_slot_not_booked_response():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     mock_date = '2020-06-14'
#     book_days_after = 8
#     present_date = "2020-06-01"
#     expected_response = "Slot Not Booked"

#     date_obj = datetime.strptime(mock_date, '%Y-%m-%d')
#     day = date_obj.strftime("%A")

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     configure_slot_storage.book_days_after.return_value = 8
#     user_slot_storage.cannot_book_in_date.return_value=False
#     presenter.slot_not_booked_response.return_value=expected_response

#     #Act
    
#     book_a_slot_response = interactor.book_a_slot(
#             user_id=user_id, date=mock_date, start_time=start_time, 
#             end_time=end_time
#     )

#     #Assert
#     configure_slot_storage.book_days_after.assert_called_once_with()
#     user_slot_storage.cannot_book_in_date.assert_called_once_with(
#             user_id, present_date, book_days_after)
#     assert book_a_slot_response == expected_response
#     presenter.slot_not_booked_response.assert_called_once_with()
    

# '''

# @freeze_time("2020-06-01")
# def test_book_a_slot_raises_exception_for_invalid_start_time():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     date = '2020-06-14'
#     book_days_after = 8
#     present_date = "2020-06-01"

#     date_obj = datetime.strptime(date, '%Y-%m-%d')
#     day = date_obj.strftime("%A")

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     configure_slot_storage.book_days_after.return_value = 8
#     user_slot_storage.cannot_book_in_date.return_value=False
#     washing_machine_slot_storage.washing_machines_in_given_slot.return_value=\
#         ['start_time']
#     presenter.raise_exception_for_invalid_start_time.side_effect=BadRequest

#     #Act
#     with pytest.raises(BadRequest):
#         interactor.book_a_slot(
#             user_id=user_id, date=date, start_time=start_time, 
#             end_time=end_time
#         )

#     #Assert
#     washing_machine_slot_storage.washing_machines_in_given_slot(
#             day, start_time, end_time
#     )
#     user_slot_storage.cannot_book_in_date.assert_called_once_with(
#             user_id, present_date, book_days_after)

#     presenter.raise_exception_for_invalid_start_time.assert_called_once_with()


# @freeze_time("2020-09-14")
# #@patch(calendar, 'day_name', return_value="Sunday")
# def test_book_a_slot_raises_exception_for_invalid_end_time():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     mock_date = '2030-06-30'
#     book_days_after = 8
#     present_date = "2020-09-14"

#     date_obj = datetime.strptime(mock_date, '%Y-%m-%d')
#     day = date_obj.strftime("%A")

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     configure_slot_storage.book_days_after.return_value = 8
#     user_slot_storage.cannot_book_in_date.return_value=False
#     washing_machine_slot_storage.washing_machines_in_given_slot.return_value=\
#         'end_time'
#     presenter.raise_exception_for_invalid_end_time.side_effect=BadRequest

#     #Act
#     with pytest.raises(BadRequest):
#         interactor.book_a_slot(
#             user_id=user_id, date=mock_date, start_time=start_time, 
#             end_time=end_time
#         )

#     #Assert
#     washing_machine_slot_storage.washing_machines_in_given_slot(
#             day, start_time, end_time
#     )
#     user_slot_storage.cannot_book_in_date.assert_called_once_with(
#             user_id, present_date, book_days_after)

#     presenter.raise_exception_for_invalid_end_time.assert_called_once_with()


# @freeze_time("2020-09-14")
# def test_book_a_slot_return_unavailable_washing_machines():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     mock_date = '2020-06-30'
#     book_days_after = 8
#     present_date = "2020-09-14"
#     expected_response = "Unavailable Washing machines"

#     date_obj = datetime.strptime(mock_date, '%Y-%m-%d')
#     day = date_obj.strftime("%A")

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     configure_slot_storage.book_days_after.return_value = 8
#     user_slot_storage.cannot_book_in_date.return_value=False
#     washing_machine_slot_storage.washing_machines_in_given_slot.return_value=["wm1"]
#     user_slot_storage.create_user_slot.return_value=False    
#     presenter.raise_exception_for_unavailable_washing_machines.side_effect=\
#         BadRequest

#     #Act
    
#     book_a_slot_response = interactor.book_a_slot(
#             user_id=user_id, date=mock_date, start_time=start_time, 
#             end_time=end_time
#     )

#     #Assert
#     washing_machine_slot_storage.washing_machines_in_given_slot(
#             day, start_time, end_time
#     )
#     user_slot_storage.cannot_book_in_date.assert_called_once_with(
#             user_id, present_date, book_days_after)

#     presenter.unavailable_washing_machines_respose.assert_called_once_with()
#     assert book_a_slot_response == expected_response

# @freeze_time("2020-09-14")
# def test_book_a_slot_create_user_slot_return_true():
#     #Arrange
#     user_id=1
#     start_time = "19:22:46.810366"
#     end_time = "20:22:46.810366"
#     mock_date = '2030-06-30'
#     book_days_after = 8
#     present_date = "2020-09-14"

#     date_obj = datetime.strptime(mock_date, '%Y-%m-%d')
#     day = date_obj.strftime("%A")

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface
#     )
#     user_slot_storage = create_autospec(UserSlotStorageInterface)
#     configure_slot_storage = create_autospec(ConfigureSlotStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = BookASlotInteractor(
#         user_slot_storage=user_slot_storage,
#         configure_slot_storage = configure_slot_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     configure_slot_storage.book_days_after.return_value = 8
#     user_slot_storage.cannot_book_in_date.return_value=False
#     washing_machine_slot_storage.washing_machines_in_given_slot.return_value=["wm1"]
#     user_slot_storage.create_user_slot.return_value=True

#     #Act
#     interactor.book_a_slot(
#             user_id=user_id, date=mock_date, start_time=start_time, 
#             end_time=end_time
#     )

#     #Assert
#     washing_machine_slot_storage.washing_machines_in_given_slot(
#             day, start_time, end_time
#     )
#     user_slot_storage.cannot_book_in_date.assert_called_once_with(
#             user_id, present_date, book_days_after)

#     user_slot_storage.create_user_slot.assert_called_once()

        

#         user_slot_response = self.user_slot_storage.create_user_slot(
#             user_id, date, start_time, end_time, washing_machines
#         )

#         unavailable_slots = not user_slot_response
#         if unavailable_slots:
#             self.presenter.raise_exception_for_unavailable_washing_machines()



#         is_invalid_start_time = "start_time" in washing_machines
#         if is_invalid_start_time:
#             self.presenter.raise_exception_for_invalid_start_time()

#         is_invalid_end_time = "end_time" in washing_machines
#         if is_invalid_end_time:
#             self.presenter.raise_exception_for_invalid_end_time()




#             self.washing_machine_slot_storage.washing_machines_in_given_slot(
#             day, start_time, end_time
#         )


#         book_days_after = self.configure_slot_storage.book_days_after()
#         is_user_invalid_date_to_book = self.user_slot_storage.cannot_book_in_date(
#             user_id, present_date, book_days_after)

#         if is_user_invalid_date_to_book:
#             self.presenter.raise_exception_for_cannot_book_in_date()


# def test_get_alloted_slots_interactor_returns_alloted_slots_dto(
#     alloted_slots_dtos):
#     #Arrange
#     washing_machine_id = "wm1"
#     day = "Monday"
#     expected_output = {
#       "alloted_slots":  [
#             {
#                 "start_time": "19:22:46.810366",
#                 "end_time": "20:22:46.810366",
#             },
#             {
#                 "start_time": "20:22:46.810366",
#                 "end_time": "21:22:46.810366",
#             }
#         ]
#     }

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface)
#     washing_machine_storage = create_autospec(WashingMachineStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = AllotedSlotsInteractor(
#         washing_machine_storage=washing_machine_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     washing_machine_slot_storage.get_alloted_slots.return_value = \
#         alloted_slots_dtos
#     presenter.get_response_for_alloted_slots.return_value = expected_output

#     #Act
#     response = interactor.get_alloted_slots(
#         day=day,
#         washing_machine_id=washing_machine_id
#     )

#     #Assert
#     washing_machine_slot_storage.get_alloted_slots.assert_called_once_with(
#         day=day, washing_machine_id=washing_machine_id)
#     presenter.get_response_for_alloted_slots.assert_called_once_with(
#         alloted_slots_dtos)
#     assert response == expected_output


# def test_get_alloted_slots_interactor_returns_alloted_slots_dto_empty(
#     alloted_slots_dtos):
#     #Arrange
#     washing_machine_id = "wm1"
#     day = "Monday"

#     expected_output = {
#       "alloted_slots":  []
#     }

#     alloted_slots_dtos = []

#     washing_machine_slot_storage = create_autospec(
#         WashingMachineSlotStorageInterface)
#     washing_machine_storage = create_autospec(WashingMachineStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = AllotedSlotsInteractor(
#         washing_machine_storage=washing_machine_storage,
#         washing_machine_slot_storage=washing_machine_slot_storage,
#         presenter=presenter
#     )

#     washing_machine_slot_storage.get_alloted_slots.return_value = \
#         alloted_slots_dtos
#     presenter.get_response_for_alloted_slots.return_value = expected_output

#     #Act
#     response = interactor.get_alloted_slots(
#         day=day,
#         washing_machine_id=washing_machine_id
#     )

#     #Assert
#     washing_machine_slot_storage.get_alloted_slots.assert_called_once_with(
#         day=day, washing_machine_id=washing_machine_id)
#     presenter.get_response_for_alloted_slots.assert_called_once_with(
#         alloted_slots_dtos)
#     assert response == expected_output

# '''
