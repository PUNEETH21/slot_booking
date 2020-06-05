# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_avaliable_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "avaliable_slots/v1/"

from .test_case_01 import TestCase01GetAvaliableSlotsAPITestCase

__all__ = [
    "TestCase01GetAvaliableSlotsAPITestCase"
]
