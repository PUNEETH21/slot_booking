# from slot_booking.interactors.storages.storage_interface import \
#     StorageInterface
# from slot_booking.interactors.presenters.presenter_interface import \
#     PresenterInterface
# from common.oauth2_storage import OAuth2SQLStorage
# from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

# class AvaliableSlotsInteractor:

#     def __init__(self, storage: StorageInterface,
#         presenter: PresenterInterface):

#         self.storage = storage
#         self.presenter = presenter

#     def avaliable_slots(self, username: str, password: str):
#         invalid_username = not self.storage.is_valid_username(
#             username=username)
#         if invalid_username:
#             self.presenter.raise_exception_for_invalid_username()

#         invalid_password = not self.storage.is_valid_password(
#             password=password)
#         if invalid_password:
#             self.presenter.raise_exception_for_invalid_password()

#         user_id = self.storage.is_valid_user_password(
#                 username=username,
#                 password=password
#             )

#         is_invalid_user_password = not user_id
#         if is_invalid_user_password:
#             self.presenter.raise_exception_for_invalid_user_password()

#         service = OAuthUserAuthTokensService(
#             oauth2_storage=self.oauth2_storage)

#         token = service.create_user_auth_tokens(
#                 user_id=1
#             )
#         print(token)

#         return self.presenter.get_response_for_login(token)




# '''


# from slot_booking.models import user
# from slot_booking.interactors.storages.storage_interface import \
#     StorageInterface
# from slot_booking.interactors.presenters.presenter_interface import \
#     PresenterInterface
# from slot_booking.interactors.login_interactor import LogInInteractor

# from common.oauth2_storage import OAuth2SQLStorage
# from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
# from unittest.mock import Mock, create_autospec

#  from slot_booking.interactors.storages import *

# storage = create_autospec(StorageInterface)
# oauth2_storage = create_autospec(OAuth2SQLStorage)
# presenter = create_autospec(PresenterInterface)
# interactor = LogInInteractor(
#         storage=storage,
#         oauth2_storage=oauth2_storage,
#         presenter=presenter
#         )


# token = interactor.login(username="username",password="password")   


# ''' 