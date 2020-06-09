from abc import ABC
from abc import abstractmethod
from typing import List


class ConfigureSlotStorageInterface(ABC):

    @abstractmethod
    def book_no_of_days_after(self):
        pass
