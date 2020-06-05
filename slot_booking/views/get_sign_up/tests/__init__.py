# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_sign_up"
REQUEST_METHOD = "post"
URL_SUFFIX = "sign_up/v1/"

from .test_case_01 import TestCase01GetSignUpAPITestCase

__all__ = [
    "TestCase01GetSignUpAPITestCase"
]
