import pytest
from flask import url_for
from flask_jwt_extended import create_access_token


@pytest.mark.usefixtures("client_class")
class TestQueries:
    def test__query_me__returns_user_data(self, user, snapshot):
        token = create_access_token(user.id, fresh=True)
        url = url_for("graphql")
        res = self.client.post(
            url,
            headers={"Authorization": "Bearer {}".format(token)},
            content_type="application/json",
            data='{"query": "query CurrentUser { me { name, avatarUrl } }" }',
        )
        snapshot.assert_match(res.data)
