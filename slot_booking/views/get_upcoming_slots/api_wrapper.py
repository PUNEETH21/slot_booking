from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.upcoming_slots_interactor \
    import UpcomingSlotsInteractor

from slot_booking.storages.user_slot_storage_implementation\
    import UserSlotStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id=kwargs["user_dto"].user_id
    user_slot_storage = UserSlotStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpcomingSlotsInteractor(
        user_slot_storage=user_slot_storage,
        presenter=presenter
    )

    upcoming_slots = interactor.get_upcoming_slots(user_id=user_id)

    data = json.dumps(upcoming_slots)
    response = HttpResponse(data, status=200)
    return response
