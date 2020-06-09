from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.book_a_slot_interactor \
    import BookASlotInteractor

from slot_booking.storages.washing_machine_slot_storage_implementation\
    import WashingMachineSlotStorageImplementation

from slot_booking.storages.user_slot_storage_implementation\
    import UserSlotStorageImplementation

from slot_booking.storages.configure_slot_storage_implementation \
    import ConfigureSlotStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id = kwargs["user_dto"].user_id
    request_data = kwargs['request_data']
    date = request_data["date"]
    start_time = request_data["start_time"]
    end_time = request_data["end_time"]
    

    user_slot_storage = UserSlotStorageImplementation()
    washing_machine_slot_storage = WashingMachineSlotStorageImplementation()
    configure_slot_storage = ConfigureSlotStorageImplementation()
    presenter = PresenterImplementation()
    interactor = BookASlotInteractor(
        washing_machine_slot_storage=washing_machine_slot_storage,
        user_slot_storage=user_slot_storage,
        configure_slot_storage=configure_slot_storage,
        presenter=presenter
    )

    slot_response = interactor.book_a_slot(
        user_id=user_id, date=date, start_time=start_time, end_time=end_time
    )

    data = json.dumps(slot_response)
    response = HttpResponse(data, status=201)
    return response
