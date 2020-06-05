from typing import List, Optional
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden

from slot_booking.interactors.storages.sign_up_storage_interface import \
    SignUpStorageInterface


class SignUpStorageImplementation(SignUpStorageInterface):


    def create_user(self, username: str, password: str):
        pass
