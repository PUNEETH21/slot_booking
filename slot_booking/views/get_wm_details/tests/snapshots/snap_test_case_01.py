# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetWmDetailsAPITestCase::test_case status'] = 400

snapshots['TestCase01GetWmDetailsAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_WASHING_MACHINE_ID',
    'response': 'Invalid Washing Machine Id, try with valid Washing Machine Id'
}

snapshots['TestCase01GetWmDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '146',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
