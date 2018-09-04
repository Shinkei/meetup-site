# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["TestLogin.test__login_url__returns_oauth_redirection 1"] = {
    "Access-Control-Allow-Origin": "*",
    "Content-Length": "589",
    "Content-Type": "text/html; charset=utf-8",
    "Location": "https://github.com/login/oauth/authorize?response_type=code&client_id=55c03bf7535a58408b2c&redirect_uri=http%3A%2F%2Ftest.local%2Flogin%2Fauthorized&scope=read%3Auser%2Cread%3Aorg",
    "Vary": "Cookie",
}

snapshots["TestLogin.test__login_url__returns_oauth_redirection 2"] = "302 FOUND"

snapshots["TestLogin.test__authorized_url__returns_jwt 1"] = {
    "_id": None,
    "avatar_url": "http://example.com/person.png",
    "email": "person@example.com",
    "events": None,
    "handle": "person",
    "import_id": "103",
    "name": "John Doe",
    "orgs": None,
    "profile_url": "http://example.com/person",
}

snapshots["TestLogin.test__authorized_url__returns_jwt 2"] = [
    {
        "_id": None,
        "avatar_url": "http://example.com/company.png",
        "handle": "example",
        "import_id": "123",
        "users": None,
    }
]
