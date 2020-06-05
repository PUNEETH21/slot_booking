# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_missed_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "missed_slots/v1/"

from .test_case_01 import TestCase01GetMissedSlotsAPITestCase

__all__ = [
    "TestCase01GetMissedSlotsAPITestCase"
]
