# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetMissedSlotsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetMissedSlotsAPITestCase::test_case body'] = {
    'no_of_missed_slots': 1
}

snapshots['TestCase01GetMissedSlotsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '24',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
