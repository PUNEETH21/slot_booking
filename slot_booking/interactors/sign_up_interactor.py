from slot_booking.interactors.storages.user_storage_interface import \
    UserStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

class SignUpInteractor:

    def __init__(self, storage: UserStorageInterface,
        presenter: PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def sign_up(self, username: str, password: str):
        invalid_username = self.storage.is_valid_username(
            username=username
        )

        if invalid_username:
            self.presenter.raise_exception_for_invalid_username()
            return 

        self.storage.create_user(username=username, password=password)

        sign_up_response = self.presenter.get_response_for_sign_up()

        return sign_up_response









'''


from slot_booking.models import user
from slot_booking.interactors.login_interactor import LogInInteractor

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from unittest.mock import Mock, create_autospec

from slot_booking.interactors.storages import *
from slot_booking.interactors.storages.storage_interface import \
    StorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface

storage = StorageInterface()
oauth2_storage = OAuth2SQLStorage()
presenter = PresenterInterface()

from slot_booking.storages.storage_implementation import \
    StorageImplementation
from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

storage = StorageImplementation()
oauth2_storage = OAuth2SQLStorage()
presenter = PresenterImplementation()
interactor = LogInInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
        )

token = interactor.login(username="username",password="password")   







storage = create_autospec(StorageInterface())
oauth2_storage = OAuth2SQLStorage()
presenter = PresenterInterface()


''' 