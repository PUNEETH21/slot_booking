from abc import ABC
from abc import abstractmethod
from typing import Optional


class SignUpStorageInterface(ABC):

    @abstractmethod
    def create_user(self, username: str, password: str):
        pass

