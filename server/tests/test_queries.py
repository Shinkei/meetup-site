import pytest
from flask import url_for
from flask_jwt_extended import create_access_token


@pytest.mark.usefixtures("client_class")
class TestQueries:
    @pytest.fixture
    def query_me(self):
        return '{"query": "query CurrentUser { me { name, avatarUrl } }" }'

    def test__query_me__authenticated__returns_user_data(
        self, user, query_me, snapshot
    ):
        token = create_access_token(user.id, fresh=True)
        url = url_for("graphql")
        res = self.client.post(
            url,
            headers={"Authorization": "Bearer {}".format(token)},
            content_type="application/json",
            data=query_me,
        )
        snapshot.assert_match(res.data)

    def test__query_me__not_authenticated__returns_errors(
        self, user, query_me, snapshot
    ):
        url = url_for("graphql")
        res = self.client.post(url, content_type="application/json", data=query_me)
        snapshot.assert_match(res.data)
