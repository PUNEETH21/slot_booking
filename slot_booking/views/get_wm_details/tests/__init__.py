# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_wm_details"
REQUEST_METHOD = "post"
URL_SUFFIX = "get_washing_machine_details/v1/"

from .test_case_01 import TestCase01GetWmDetailsAPITestCase

__all__ = [
    "TestCase01GetWmDetailsAPITestCase"
]
