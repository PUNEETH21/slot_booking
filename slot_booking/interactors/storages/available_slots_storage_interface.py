from abc import ABC
from abc import abstractmethod
from typing import Optional


class AvailableSlotsStorageInterface(ABC):

    @abstractmethod
    def get_available_slots(self):
        pass
