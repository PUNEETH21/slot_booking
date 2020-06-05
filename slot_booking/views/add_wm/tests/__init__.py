# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "add_wm"
REQUEST_METHOD = "post"
URL_SUFFIX = "add_washing_machine/v1/"

from .test_case_01 import TestCase01AddWmAPITestCase

__all__ = [
    "TestCase01AddWmAPITestCase"
]
