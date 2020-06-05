# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_login"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01GetLoginAPITestCase

__all__ = [
    "TestCase01GetLoginAPITestCase"
]
