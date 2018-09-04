import pytest
from collections import namedtuple
from unittest.mock import patch
from flask import url_for
from dojo.login import github
from dojo.models import User


@pytest.mark.usefixtures("client_class")
class TestLogin:
    @pytest.fixture(scope="function")
    def mock_gh_authorized_response(self):
        with patch.object(github, "authorized_response") as _:
            yield _

    @pytest.fixture(scope="function")
    def mock_gh_get(self):
        with patch.object(github, "get") as _:
            yield _

    def test__login_url__returns_oauth_redirection(self, snapshot):
        url = url_for("login.login")
        res = self.client.get(url)
        headers = dict(res.headers)
        del headers["Set-Cookie"]
        snapshot.assert_match(headers)
        snapshot.assert_match(res.status)

    def test__authorized_url__returns_jwt(
        self, mock_gh_authorized_response, mock_gh_get, snapshot
    ):
        mock_gh_authorized_response.return_value = {"access_token": "supersecret"}
        Object = namedtuple("Object", "data")
        mock_gh_get.side_effect = [
            Object(
                {
                    "id": 103,
                    "avatar_url": "http://example.com/person.png",
                    "html_url": "http://example.com/person",
                    "login": "person",
                    "name": "John Doe",
                    "email": "person@example.com",
                }
            ),
            Object(
                [
                    {
                        "id": 123,
                        "avatar_url": "http://example.com/company.png",
                        "login": "example",
                    }
                ]
            ),
        ]
        url = url_for("login.authorized")
        res = self.client.get(url)
        assert res.data.find(b"TOKEN") != -1
        user = User.query.filter_by(import_id=103).one()
        snapshot.assert_match(dict(user, _id=None, orgs=None, events=None))
        orgs = [dict(org, _id=None, users=None) for org in user.orgs]
        snapshot.assert_match(orgs)
