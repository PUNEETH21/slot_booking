from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.available_slots_interactor \
    import AvailableSlotsInteractor

from slot_booking.storages.user_slot_storage_implementation \
    import UserSlotStorageImplementation

from slot_booking.storages.configure_slot_storage_implementation \
    import ConfigureSlotStorageImplementation

from slot_booking.storages.washing_machine_slot_storage_implementation\
    import WashingMachineSlotStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation

import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id=kwargs["user_dto"].user_id
    user_slot_storage = UserSlotStorageImplementation()
    configure_slot_storage = ConfigureSlotStorageImplementation()
    washing_machine_slot_storage = WashingMachineSlotStorageImplementation()
    presenter = PresenterImplementation()
    print(user_id)
    interactor = AvailableSlotsInteractor(
        user_slot_storage=user_slot_storage,
        configure_slot_storage=configure_slot_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    #user_id=3
    available_slots = interactor.available_slots(user_id=user_id)
    print("#"*33, user_id)
    data = json.dumps(available_slots)
    
    response = HttpResponse(data, status=200)
    return response
