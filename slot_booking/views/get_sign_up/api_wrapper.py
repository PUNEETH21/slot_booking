from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.sign_up_interactor \
    import SignUpInteractor

from slot_booking.storages.user_storage_implementation\
    import UserStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter
    )

    sign_up_response = interactor.sign_up(username=username, password=password)

    data = json.dumps(sign_up_response)
    response = HttpResponse(data, status=201)
    return response
