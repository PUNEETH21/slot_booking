from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.previous_slots_interactor \
    import PreviousSlotsInteractor

from slot_booking.storages.user_slot_storage_implementation\
    import UserSlotStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id=kwargs["user_dto"].user_id
    off_set = kwargs["request_query_params"].off_set
    limit = kwargs["request_query_params"].limit

    user_slot_storage = UserSlotStorageImplementation()
    presenter = PresenterImplementation()
    interactor = PreviousSlotsInteractor(
        user_slot_storage=user_slot_storage,
        presenter=presenter
    )

    previous_slots = interactor.get_previous_slots(
        user_id=user_id, off_set=off_set, limit=limit)

    data = json.dumps(previous_slots)
    response = HttpResponse(data, status=200)
    return response
