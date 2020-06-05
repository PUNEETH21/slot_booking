# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_washing_machine_slots"
REQUEST_METHOD = "post"
URL_SUFFIX = "washing_machine_slots/v1/"

from .test_case_01 import TestCase01GetWashingMachineSlotsAPITestCase

__all__ = [
    "TestCase01GetWashingMachineSlotsAPITestCase"
]
