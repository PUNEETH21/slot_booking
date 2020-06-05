from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.login_interactor \
    import LogInInteractor

from slot_booking.storages.user_storage_implementation\
    import UserStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    storage = UserStorageImplementation()
    oauth2_storage = OAuth2SQLStorage() 
    presenter = PresenterImplementation()
    interactor = LogInInteractor(
        storage=storage,
        oauth2_storage = oauth2_storage,
        presenter=presenter
    )

    user_details = interactor.login(username=username, password=password)

    data = json.dumps(user_details)
    response = HttpResponse(data, status=200)
    return response
