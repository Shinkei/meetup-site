# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "TestQueries.test__query_me__returns_user_data 1"
] = b'{"data":{"me":{"name":"Foo Bar","avatarUrl":"...img"}}}'
