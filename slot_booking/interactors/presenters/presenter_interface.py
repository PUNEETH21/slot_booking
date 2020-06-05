from abc import ABC
from abc import abstractmethod
# from slot_booking.dtos.dtos import AvailableSlotsDto
from slot_booking.dtos.dtos import (
    TimeSlotDto, PreviousSlotDto, PreviousSlotsDto, 
    WashingMachineSlotsDto, UpcomingSlotDto, UserAuthTokensDto,
    WashingMachineDetailsDto
)

class PresenterInterface(ABC):

    @abstractmethod
    def is_valid_password(self, password: str):
        pass

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_username_password(self):
        pass

    @abstractmethod
    def get_response_for_login(self, token_details_dto: UserAuthTokensDto):
        pass

    @abstractmethod
    def get_response_for_sign_up(self):
        pass

    # @abstractmethod
    # def get_available_slots_response(
    #     self, available_slots_dto: AvailableSlotsDto
    # ):
    #     pass

    @abstractmethod
    def raise_exception_for_invalid_washing_machine_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_day(self):
        pass

    @abstractmethod
    def get_response_for_washing_machine_slots(self, washing_machine_slots_dto):
        pass

    @abstractmethod
    def get_response_for_previous_slots(self, previous_slots_dto):
        pass

    @abstractmethod
    def get_response_for_upcoming_slots(self, upcoming_slots_dto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_date(self):
        pass

    @abstractmethod
    def raise_exception_for_cannot_book_in_date(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_start_time(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_end_time(self):
        pass

    @abstractmethod
    def slot_not_booked_response(self):
        pass

    @abstractmethod
    def slot_booked_response(self):
        pass

    @abstractmethod
    def unavailable_washing_machines_response(self):
        pass

    @abstractmethod
    def get_response_for_add_washing_machine(self):
        pass

    @abstractmethod
    def get_response_for_get_washing_machine_details(self, 
        washing_machine_details_dto: WashingMachineDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_washing_machine_id_already_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_time_slot(self):
        pass

    @abstractmethod
    def get_response_for_update_time_slots(self):
        pass


    @abstractmethod
    def get_response_for_available_slots(self, available_slots_dtos: list):
        pass

