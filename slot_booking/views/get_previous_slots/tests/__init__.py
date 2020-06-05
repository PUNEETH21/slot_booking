# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_previous_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "previous_slots/v1/"

from .test_case_01 import TestCase01GetPreviousSlotsAPITestCase

__all__ = [
    "TestCase01GetPreviousSlotsAPITestCase"
]
