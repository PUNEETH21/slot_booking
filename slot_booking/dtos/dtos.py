from dataclasses import dataclass
from datetime import datetime
from slot_booking.constants.enums import Day
from typing import List, Dict
from datetime import time
from datetime import date

@dataclass
class UserAuthTokensDto:
    is_admin: bool
    access_token : str
    refresh_token : str
    expires_in: datetime


@dataclass
class TimeSlotDto:
    start_time : str
    end_time : str

@dataclass
class WashingMachineSlotsDto:
    washing_machine_slots_dtos : List[TimeSlotDto]

@dataclass
class PreviousSlotDto:
    date: str
    start_time: str
    end_time: str
    washing_machine_id: str

@dataclass
class UpcomingSlotDto:
    date: str
    start_time: str
    end_time: str
    washing_machine_id: str

@dataclass
class PreviousSlotsDto:
    previous_slots: List[PreviousSlotDto]

@dataclass
class WashingMachineDto:
    wm_id : str

@dataclass
class WashingMachineDetailsDto:
    washing_machine_id : str
    is_active : bool

@dataclass
class UpdateTimeSlotDto:
    day : str
    washing_machine_id : str
    time_slots_dtos : list

@dataclass
class AvailableTimeSlotDto:
    start_time : str
    end_time : str
    is_available : bool


@dataclass
class TimeRangeCountDto:
    start_time : str
    end_time : str
    count : str

@dataclass
class AvailableSlotsDtos:
    date : str
    time_slots : List[AvailableTimeSlotDto]



'''
@dataclass
class TimeSlotDto:
    start_time : str
    end_time : str

@dataclass
class TimeSlotsDtos:
    time_slots : List[TimeSlotDto]

@dataclass
class AllotedSlotsDto:
    alloted_slots : TimeSlotsDtos


@dataclass
class AvailableSlotDto:
    date: date
    start_time : List[time]
    end_time : List[time]
    is_available : List[bool]

@dataclass
class AvailableSlotsDto:
    present_date: date
    time_slots: List[Dict[TimeSlotsDto]]
    
        
@dataclass
class WashingMachineSlotsDto:
    present_date: date
    time_ranges : List[List[int]] 

@dataclass
class UserSlotsDto:
    present_date: date
    time_ranges : List[List[int]]

@dataclass
class AvailableSlotsStorageDto:
    washing_machine_slots_dtos: List[WashingMachineSlotsDto]
    user_slots_dtos: List[UserSlotsDto]
    washing_machines_count : int

@dataclass
class AvailableSlotsPresenterDto:
    available_slots_dtos: List[Dict[AvailableSlotsDto]]
    

'''