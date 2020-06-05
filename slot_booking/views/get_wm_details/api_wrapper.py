from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.get_washing_machine_details_interactor \
    import GetWashingMachineDetailsInteractor

from slot_booking.storages.washing_machine_storage_implementation\
    import WashingMachineStorageImplementation

from slot_booking.presenters.presenter_implementation import \
    PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data = kwargs['request_data']
    washing_machine_id = request_data['washing_machine_id']

    washing_machine_storage = WashingMachineStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetWashingMachineDetailsInteractor(
        washing_machine_storage=washing_machine_storage,
        presenter=presenter
    )

    details_response = interactor.get_washing_machine_details(
                      washing_machine_id=washing_machine_id)

    data = json.dumps(details_response)
    response = HttpResponse(data, status=200)
    return response
