from abc import ABC
from abc import abstractmethod
from typing import Optional


class WashingMachineStorageInterface(ABC):

    @abstractmethod
    def is_valid_washing_machine_id(self, washing_machine_id: str):
        pass

    @abstractmethod
    def add_washing_machine(self, washing_machine_id: str, is_active: bool):
        pass

    @abstractmethod
    def get_washing_machine_details(self, washing_machine_id: str):
        pass

