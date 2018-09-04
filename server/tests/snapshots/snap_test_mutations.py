# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "TestQueries.test__mutation_save_event__not_authenticated__returns_errors 1"
] = b'{"errors":[{"message":"Authentication failed","locations":[{"line":1,"column":53}],"path":["saveEvent"]}],"data":{"saveEvent":null}}'

snapshots[
    "TestQueries.test__mutation_save_event__authenticated__returns_query_data 1"
] = b'{"data":{"saveEvent":{"new":true}}}'

snapshots[
    "TestQueries.test__mutation_save_event__given_id__updates_record 1"
] = b'{"data":{"saveEvent":{"new":false,"event":{"date":"2018-09-02T01:07:03.112000","location":[-75.536111,6.291389]}}}}'
