from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.update_washing_machine_slots_interactor \
    import UpdateWashingMachineSlotsInteractor

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

    request_data = kwargs["request_data"]

    day = request_data['day']
    washing_machine_id = request_data['washing_machine_id']
    time_slots = request_data['time_slots']

    washing_machine_storage = WashingMachineStorageImplementation()
    washing_machine_slot_storage = WashingMachineSlotStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateWashingMachineSlotsInteractor(
        washing_machine_storage=washing_machine_storage,
        washing_machine_slot_storage=washing_machine_slot_storage,
        presenter=presenter
    )

    update_response = interactor.update_washing_machine_slots(
        day = day,
        washing_machine_id=washing_machine_id,
        time_slots = time_slots
    )

    data = json.dumps(update_response)
    response = HttpResponse(data, status=200)
    return response
