from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

from slot_booking.constants.exception_messages import (
    INVALID_USERNAME_EXCEPTION, INVALID_PASSWORD_EXCEPTION, 
    INVALID_DAY_EXCEPTION ,INVALID_WASHING_MACHINE_ID_EXCEPTION,
    INVALID_USERNAME_PASSWORD_EXCEPTION, INVALID_DATE_EXCEPTION, 
    INVALID_END_TIME_EXCEPTION, INVALID_START_TIME_EXCEPTION, 
    UNAVAILABLE_WASHING_MACHINES_EXCEPTION, CANNOT_BOOK_IN_DATE_EXCEPTION,
    WASHING_MACHINE_ID_ALREADY_EXIST_EXCEPTION,
    INVALID_TIME_SLOTS_EXCEPTION, NO_SLOTS_IN_GIVEN_DATE_EXCEPTION,
    INVALID_TIME_SLOT_EXCEPTION
    )
    
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from slot_booking.dtos.dtos import (
    WashingMachineSlotsDto, PreviousSlotDto, TimeSlotDto, UpcomingSlotDto,
    UserAuthTokensDto, WashingMachineDetailsDto
)

from typing import List

class PresenterImplementation(PresenterInterface):


    def is_valid_password(self, password: str):
        pass


    def raise_exception_for_invalid_username(self):
        raise BadRequest(*INVALID_USERNAME_EXCEPTION)


    def raise_exception_for_invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD_EXCEPTION)


    def raise_exception_for_invalid_username_password(self):
        raise BadRequest(*INVALID_USERNAME_PASSWORD_EXCEPTION)


    def get_response_for_login(self, token_details_dto: UserAuthTokensDto):
        response_dict = {}
        response_dict["is_admin"] = token_details_dto.is_admin
        response_dict["access_token"] = token_details_dto.access_token
        response_dict["refresh_token"] = token_details_dto.refresh_token
        response_dict["expires_in"] = str(token_details_dto.expires_in)

        return response_dict

    def get_response_for_sign_up(self):
        sign_up_response = "User Created Successfully"
        return sign_up_response

    def raise_exception_for_invalid_washing_machine_id(self):
        raise BadRequest(*INVALID_WASHING_MACHINE_ID_EXCEPTION)

    def raise_exception_for_invalid_day(self):
        raise BadRequest(*INVALID_DAY_EXCEPTION)

    def get_response_for_washing_machine_slots(self, 
        washing_machine_slots_dtos: List[TimeSlotDto]):

        washing_machine_slots_list = []
        if washing_machine_slots_dtos:
            for washing_machine_slot_dto in washing_machine_slots_dtos:
                washing_machine_slot_dict = {}
                washing_machine_slot_dict["start_time"] = washing_machine_slot_dto.start_time
                washing_machine_slot_dict["end_time"] = washing_machine_slot_dto.end_time

                washing_machine_slots_list.append(washing_machine_slot_dict)
        
        washing_machine_slots_dict = {'washing_machine_slots': washing_machine_slots_list}
        return washing_machine_slots_dict


    def get_response_for_previous_slots(self, 
        previous_slots_dtos: List[PreviousSlotDto]):

        previous_slots_list = []
        if previous_slots_dtos:
            for previous_slots_dto in previous_slots_dtos:
                previous_slots_dict = {}
                previous_slots_dict["date"] = previous_slots_dto.date
                previous_slots_dict["start_time"] = \
                    previous_slots_dto.start_time
                previous_slots_dict["end_time"] = previous_slots_dto.end_time
                previous_slots_dict["washing_machine_id"] = \
                    previous_slots_dto.washing_machine_id

                previous_slots_list.append(previous_slots_dict)

        previous_slots_dict = {"previous_slots": previous_slots_list}

        return previous_slots_dict


    def get_response_for_upcoming_slots(self, 
        upcoming_slots_dtos: List[UpcomingSlotDto]):

        upcoming_slots_list = []
        if upcoming_slots_dtos:
            for upcoming_slots_dto in upcoming_slots_dtos:
                upcoming_slots_dict = {}
                upcoming_slots_dict["date"] = upcoming_slots_dto.date
                upcoming_slots_dict["start_time"] = \
                    upcoming_slots_dto.start_time
                upcoming_slots_dict["end_time"] = upcoming_slots_dto.end_time
                upcoming_slots_dict["washing_machine_id"] = \
                    upcoming_slots_dto.washing_machine_id

                upcoming_slots_list.append(upcoming_slots_dict)

        upcoming_slots_dict = {"upcoming_slots": upcoming_slots_list}

        return upcoming_slots_dict


    def raise_exception_for_invalid_date(self):
        raise BadRequest(*INVALID_DATE_EXCEPTION)


    def raise_exception_for_cannot_book_in_date(self):
        raise BadRequest(*CANNOT_BOOK_IN_DATE_EXCEPTION)


    def raise_exception_for_no_slots_in_given_date(self):
        raise BadRequest(*NO_SLOTS_IN_GIVEN_DATE_EXCEPTION)


    def raise_exception_for_invalid_start_time(self):
        raise BadRequest(*INVALID_START_TIME_EXCEPTION)


    def raise_exception_for_invalid_end_time(self):
        raise BadRequest(*INVALID_END_TIME_EXCEPTION)


    def raise_exception_for_invalid_time_slot(self):
        raise BadRequest(*INVALID_TIME_SLOT_EXCEPTION)


    def get_response_for_unavailable_washing_machines(self):
        return "Unavailable Washing Machines Slot Not Booked"


    def get_response_for_slot_booked(self):
        return "Slot Booked Successfully"


    def get_response_for_slot_not_booked(self):
        return "Slot Not Booked"


    def get_response_for_add_washing_machine(self):
        response =  "Washing Machine Added Successfully"
        return response


    def get_response_for_get_washing_machine_details(self,
        washing_machine_details_dto: WashingMachineDetailsDto):

        response = {}
        if washing_machine_details_dto:
            response["washing_machine_id"] = \
                washing_machine_details_dto.washing_machine_id
            response["is_active"] = washing_machine_details_dto.is_active

        return response

    def raise_exception_for_washing_machine_id_already_exist(self):
        raise BadRequest(*WASHING_MACHINE_ID_ALREADY_EXIST_EXCEPTION)


    def raise_exception_for_invalid_time_slots(self):
        raise BadRequest(*INVALID_TIME_SLOTS_EXCEPTION)


    def get_response_for_update_time_slots(self):
        update_response = "Successfully Update The Washing Machine Slots"
        return update_response


    def get_response_for_available_slots(self, available_slots_dtos: list):
        available_slots_list = []

        for available_slot_dtos in available_slots_dtos:
            time_slot_dtos = available_slot_dtos.time_slots
            available_slots_dict = {}
            time_slots_list = []

            for time_slot_dto in time_slot_dtos:
                time_slot_dict = {}
                time_slot_dict["start_time"] = time_slot_dto.start_time
                time_slot_dict["end_time"] = time_slot_dto.end_time
                time_slot_dict["is_available"] = time_slot_dto.is_available

                time_slots_list.append(time_slot_dict)

            available_slots_dict["date"] = str(available_slot_dtos.date)
            available_slots_dict["time_slots"] = time_slots_list

            available_slots_list.append(available_slots_dict)

        available_slots_response = {"available_slots" : available_slots_list}
        return available_slots_response

