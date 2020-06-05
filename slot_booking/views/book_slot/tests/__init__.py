# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "book_slot"
REQUEST_METHOD = "post"
URL_SUFFIX = "book_a_slot/v1/"

from .test_case_01 import TestCase01BookSlotAPITestCase

__all__ = [
    "TestCase01BookSlotAPITestCase"
]
