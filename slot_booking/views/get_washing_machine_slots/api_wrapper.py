from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.washing_machine_slots_interactor \
    import WashingMachineSlotsInteractor

from slot_booking.storages.washing_machine_storage_implementation\
    import WashingMachineStorageImplementation

from slot_booking.storages.washing_machine_slot_storage_implementation\
    import WashingMachineSlotStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data = kwargs['request_data']
    day = request_data['day']
    washing_machine_id = request_data['washing_machine_id']

    washing_machine_storage = WashingMachineStorageImplementation()
    washing_machine_slot_storage = WashingMachineSlotStorageImplementation()
    presenter = PresenterImplementation()
    interactor = WashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    washing_machine_slots = interactor.get_washing_machine_slots(day=day,
                      washing_machine_id=washing_machine_id)

    data = json.dumps(washing_machine_slots)
    response = HttpResponse(data, status=200)
    return response
