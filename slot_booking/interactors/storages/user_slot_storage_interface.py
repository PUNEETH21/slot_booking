from abc import ABC
from abc import abstractmethod
from typing import List


class UserSlotStorageInterface(ABC):

    @abstractmethod
    def get_previous_slots(self, user_id: int, off_set: int, limit:int):
        pass

    @abstractmethod
    def get_upcoming_slots(self, user_id: int):
        pass

    @abstractmethod
    def last_used_date(self, user_id: int):
        pass

    @abstractmethod
    def available_washing_machine(self, user_slot_wm_ids: list,
        washing_machines_ids: list
    ):
        pass


    @abstractmethod
    def create_slot(self, date: str, start_time: str, 
        end_time: str, washing_machine_id: str, user_id: int
    ):
        pass

    @abstractmethod
    def create_user_slot(self, user_id: int, date: str, start_time: str, 
        end_time: str, washing_machines_ids: List[int]
    ):
        pass


    @abstractmethod
    def get_date_slots(self, date: str):
        pass

'''
    @abstractmethod
    def cannot_book_in_date(self, user_id: int, present_date: str,
        book_days_after: int
    ):
        pass
'''
