# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "TestQueries.test__query_me__authenticated__returns_user_data 1"
] = b'{"data":{"me":{"name":"Foo Bar","avatarUrl":"...img"}}}'

snapshots[
    "TestQueries.test__query_me__not_authenticated__returns_errors 1"
] = b'{"errors":[{"message":"Authentication failed","locations":[{"line":1,"column":21}],"path":["me"]}],"data":{"me":null}}'
