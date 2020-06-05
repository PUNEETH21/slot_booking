from slot_booking.interactors.storages.user_storage_interface import \
    UserStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from slot_booking.dtos.dtos import UserAuthTokensDto

class LogInInteractor:

    def __init__(self, storage: UserStorageInterface,
        oauth2_storage : OAuth2SQLStorage,
        presenter: PresenterInterface):

        self.oauth2_storage = oauth2_storage
        self.storage = storage
        self.presenter = presenter

    def login(self, username: str, password: str):
        invalid_username = not self.storage.is_valid_username(
            username=username
        )
        if invalid_username:
            self.presenter.raise_exception_for_invalid_username()

        invalid_password = not self.storage.is_valid_password(
            password=password)
        if invalid_password:
            self.presenter.raise_exception_for_invalid_password()

        user_obj = self.storage.is_valid_username_password(
                username=username,
                password=password
            )

        is_invalid_user_password = not user_obj
        if is_invalid_user_password:
            self.presenter.raise_exception_for_invalid_username_password()
            return

        service = OAuthUserAuthTokensService(
            self.oauth2_storage)

        user_id = user_obj.id
        token_details_dto = service.create_user_auth_tokens(user_id)

        token_details = UserAuthTokensDto(
            is_admin = user_obj.is_admin,
            access_token = token_details_dto.access_token,
            refresh_token = token_details_dto.refresh_token,
            expires_in = token_details_dto.expires_in
        )

        response = self.presenter.get_response_for_login(token_details)

        return response




'''


from slot_booking.models import user
from slot_booking.interactors.login_interactor import LogInInteractor

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from unittest.mock import Mock, create_autospec

from slot_booking.storages.user_storage_implementation import \
    UserStorageImplementation
from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

storage = UserStorageImplementation()
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