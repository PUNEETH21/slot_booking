from abc import ABC
from abc import abstractmethod
from typing import List


class ConfigureSlotStorageInterface(ABC):

    @abstractmethod
    def book_days_after(self):
        pass
