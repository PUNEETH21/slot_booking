from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.add_washing_machine_interactor \
    import AddWashingMachineInteractor

from slot_booking.storages.washing_machine_storage_implementation\
    import WashingMachineStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    washing_machine_id = request_data['washing_machine_id']

    washing_machine_storage = WashingMachineStorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddWashingMachineInteractor(
        washing_machine_storage=washing_machine_storage,
        presenter=presenter
    )

    add_response = interactor.add_washing_machine(
         washing_machine_id=washing_machine_id,
    )

    data = json.dumps(add_response)
    response = HttpResponse(data, status=201)
    return response
