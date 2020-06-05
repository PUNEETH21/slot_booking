from abc import ABC
from abc import abstractmethod
from typing import Optional
from slot_booking.constants.constants import DAY_CHOICES

class WashingMachineSlotStorageInterface(ABC):

    @abstractmethod
    def get_washing_machine_slots(self, day: str, washing_machine_id: str):
        pass

    @abstractmethod
    def update_slot(self, day: str, start_time: str, end_time: str,
        washing_machine_id: str):
        pass

    @abstractmethod
    def washing_machines_in_given_slot(self, day: str, start_time: str, 
        end_time: str
    ):
        pass

    @abstractmethod
    def update_time_slots(self, time_slots_dtos: list):
        pass

    @abstractmethod
    def get_day_slots(self, day: str):
        pass
