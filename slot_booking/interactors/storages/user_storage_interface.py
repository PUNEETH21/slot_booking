from abc import ABC
from abc import abstractmethod
from typing import Optional


class UserStorageInterface(ABC):

    @abstractmethod
    def is_valid_username(self, username: int):
        pass

    @abstractmethod
    def is_valid_username_password(self, username: str, password: str) -> \
        Optional:
        pass

    @abstractmethod
    def create_user(self, username: str, password: str):
        pass

