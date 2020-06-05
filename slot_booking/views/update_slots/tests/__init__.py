# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "update_slots"
REQUEST_METHOD = "post"
URL_SUFFIX = "update_washing_machine_slots/v1/"

from .test_case_01 import TestCase01UpdateSlotsAPITestCase

__all__ = [
    "TestCase01UpdateSlotsAPITestCase"
]
