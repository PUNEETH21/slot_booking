# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_upcoming_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "upcoming_slots/v1/"

from .test_case_01 import TestCase01GetUpcomingSlotsAPITestCase

__all__ = [
    "TestCase01GetUpcomingSlotsAPITestCase"
]
