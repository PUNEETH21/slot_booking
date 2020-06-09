from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface
from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.storages.configure_slot_storage_interface \
    import ConfigureSlotStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from datetime import datetime, timedelta

from slot_booking.dtos.dtos import AvailableTimeSlotDto, AvailableSlotsDtos


class AvailableSlotsInteractor:

    def __init__(self, user_slot_storage: UserSlotStorageInterface,
        configure_slot_storage: ConfigureSlotStorageInterface,
        washing_machine_slot_storage: WashingMachineSlotStorageInterface,
        presenter: PresenterInterface):

        self.user_slot_storage = user_slot_storage
        self.washing_machine_slot_storage = washing_machine_slot_storage
        self.configure_slot_storage = configure_slot_storage
        self.presenter = presenter


    def _configure_days_to_book(self, user_id: int):

        user_last_booked_date = self.user_slot_storage.last_used_date(
            user_id)

        configure_count = self.configure_slot_storage.book_no_of_days_after()

        if user_last_booked_date:
            present_date = datetime.now().date()
            date_diff = present_date - user_last_booked_date
            not_valid = date_diff.days < configure_count
            if not_valid:
                configure_count=0
        print(configure_count, 33, user_last_booked_date)
        return configure_count


    def _dates_list(self, present_date, configure_days_to_book):
        dates_list = []
        for count in range(configure_days_to_book):
            date = present_date + timedelta(count)
            dates_list.append(date)

        return dates_list

    def _days_list(self, dates):
        day_list = []
        for date in dates:
            day = date.strftime("%A")
            day_list.append(day)
    
        return day_list


    def _is_available(self, user_slot, wm_slot):
        available = user_slot.count == wm_slot.count
        if available:
            return False
        return True


    def _get_user_and_wm_slots_dtos(self, user_slot_dtos, wm_slot_dtos):
        wm_dtos = []
        for wm_slot in wm_slot_dtos:
            is_available = True
            for user_slot in user_slot_dtos:
                equal_start_time = user_slot.start_time == wm_slot.start_time
                equal_end_time = user_slot.end_time == wm_slot.end_time
                same_time = equal_start_time and equal_end_time
                if same_time:
                    is_available=self._is_available(user_slot, wm_slot)
                    break

            wm_dtos.append(
                AvailableTimeSlotDto(
                    start_time = wm_slot.start_time,
                    end_time = wm_slot.end_time,
                    is_available = is_available
                )
            )

        return wm_dtos


    def _get_wm_slots_dtos(self, wm_slot_dtos):
        wm_dtos = []
        for wm_slot in wm_slot_dtos:
            wm_dtos.append(
                AvailableTimeSlotDto(
                    start_time = wm_slot.start_time,
                    end_time = wm_slot.end_time,
                    is_available = True
                )
            )

        return wm_dtos


    def _available_slots_response(self, available_slots_dtos_list):
        available_slots_response = \
            self.presenter.get_response_for_available_slots(
                available_slots_dtos_list
            )

        return available_slots_response


    def available_slots(self, user_id: int):
        #print("a"*10)
        configure_days_to_book = self._configure_days_to_book(user_id)

        user_not_valid_to_book = not configure_days_to_book
        if user_not_valid_to_book:
            #print("b"*20)
            available_slots_dtos_list = []
            available_slots_response = self._available_slots_response(
                available_slots_dtos_list
            )

            return available_slots_response
        
        present_date = datetime.now().date()
        dates_list = self._dates_list(present_date, configure_days_to_book)
        days_list = self._days_list(dates_list)
        available_slots_dtos_list = []
        
        for count in range(configure_days_to_book):
            day = days_list[count]
            date = dates_list[count]
            wm_slot_dtos = self.washing_machine_slot_storage.get_day_slots(day)
            user_slot_dtos = self.user_slot_storage.get_date_slots(date)

            if user_slot_dtos:
                time_slots = self._get_user_and_wm_slots_dtos(
                    user_slot_dtos, wm_slot_dtos)
            else:
                time_slots = self._get_wm_slots_dtos(wm_slot_dtos)

            available_slots_dtos_list.append(
                AvailableSlotsDtos(
                    date=date,
                    time_slots=time_slots
                )
            )
        
        available_slots_response = self._available_slots_response(
            available_slots_dtos_list
        )
        print(available_slots_response)
        return available_slots_response




# from slot_booking.interactors.storages.available_slots_storage_interface \
#     import AvailableSlotsStorageInterface
# from slot_booking.interactors.presenters.presenter_interface imporot \
#     PresenterInterface

# class AvailableSlotsInteractor:

#     def __init__(self, storage: AvailableSlotsStorageInterface,
#         presenter: PresenterInterface):

#         self.storage = storage
#         self.presenter = presenter

#     def available_slots(self):
#         storage_dto = self.storage.get_available_slots()

#         user_slots_dtos = storage_dto.user_slots_dtos
#         washing_machine_slots_dtos = storage_dto.washing_machine_slots_dtos
#         washing_machines_count = storage_dto.washing_machine_count
        
#         storage_dtos_list = []
#         time_slots_list = []
#         for washing_machine_slot_dto in washing_machine_slots_dtos:
#             washing_machine_time_ranges_list = washing_machine_slot_dto.time_ranges
#             user = 0
#             for user_slots_dto in user_slots_dtos:
#                 user_slots_time_ranges_list = user_slots_dto.time_ranges
#                 is_washing_machine_slot_used = \
#                     washing_machine_slot_dto.present_date== \
#                     user_slots_dto.present_date

#                 if is_washing_machine_slot_used:
#                     user = user_slots_dto
#                     break

#             for washing_machine_time_range in washing_machine_time_ranges_list:
#                 washings_count = 0
#                 if user:
#                     user_slot_time_ranges = user_slots_dto.time_ranges
#                     washings_count = no_of_washings(
#                         washing_machine_time_range, user_slot_time_ranges
#                         )
#                 not_available_count = washings_count == washing_machines_count

#                 if not_available_count:
#                     available = False
#                 else:
#                     available = True
                
#                 time_slots_list.append(
#                         TimeSlotsDto(
#                             start_time = washing_machine_time_range[0],
#                             end_time = washing_machine_time_range[1],
#                             is_available = available
#                     )
#                 )    
#             storage_dtos_list.append(
#                 AvailableSlotsDto(
#                     present_date = washing_machine_slot_dto.present_date,
#                     time_slots = time_slots_list
#                     )
#                 )

#         available_slots_storage_dto = AvailableSlotsPresenterDto(
#             available_slots_dto= storage_dtos_list
#             )
#         available_slots = self.presenter.get_available_slots_response(
#             available_slots_storage_dto)
#         return available_slots
    
#     def no_of_washings(self, washing_machine_time_range,
#     user_slots_time_ranges_list):
#         count = 0
#         for user_slot_time_range in user_slots_time_ranges_list:
#             is_time_slot_equal = (
#                 user_slot_time_range[0]== washing_machine_time_range[0] \
#                 and user_slot_time_range[1]==washing_machine_time_range[1]
#             )
#             if is_time_slot_equal:
#                 count+=1

#         return count

# '''
# @dataclass
# class TimeSlotsDto:
#     start_time: time
#     end_time: time
#     is_available: bool

# @dataclass
# class AvailableSlotsDto:
#     present_date: date
#     time_slots: List[Dict[TimeSlotsDto]]
    
    
# @dataclass
# class WashingMachineSlotsDto:
#     present_date: date
#     time_ranges : List[List[int]] 

# @dataclass
# class UserSlotsDto:
#     present_date: date
#     time_ranges : List[List[int]]

# @dataclass
# class AvailableSlotsStorageDto:
#     washing_machine_slots_dtos: List[WashingMachineSlotsDto]
#     user_slots_dtos: List[UserSlotsDto]
#     washing_machines_count : int

# @dataclass
# class AvailableSlotsPresenterDto:
#     available_slots_dtos: List[Dict[AvailableSlotsDto]]
# '''















# '''


# from slot_booking.models import user
# from slot_booking.interactors.login_interactor import LogInInteractor

# from common.oauth2_storage import OAuth2SQLStorage
# from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
# from unittest.mock import Mock, create_autospec

# from slot_booking.interactors.storages import *
# from slot_booking.interactors.storages.storage_interface import \
#     StorageInterface
# from slot_booking.interactors.presenters.presenter_interface import \
#     PresenterInterface

# storage = StorageInterface()
# oauth2_storage = OAuth2SQLStorage()
# presenter = PresenterInterface()

# from slot_booking.storages.storage_implementation import \
#     StorageImplementation
# from slot_booking.presenters.presenter_implementation import \
#     PresenterImplementation

# storage = StorageImplementation()
# oauth2_storage = OAuth2SQLStorage()
# presenter = PresenterImplementation()
# interactor = LogInInteractor(
#         storage=storage,
#         oauth2_storage=oauth2_storage,
#         presenter=presenter
#         )

# token = interactor.login(username="username",password="password")   







# storage = create_autospec(StorageInterface())
# oauth2_storage = OAuth2SQLStorage()
# presenter = PresenterInterface()


# ''' 