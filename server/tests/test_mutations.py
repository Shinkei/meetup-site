import pytest
from flask import url_for
from flask_jwt_extended import create_access_token


@pytest.mark.usefixtures("client_class")
class TestQueries:
    @pytest.fixture
    def mutation_new_event(self):
        return """
        {
            "query": "mutation NewEvent($date: DateTime) {\
                saveEvent(date: $date) { new }\
            }",
            "variables": {"date": "2018-09-01T11:00:00"}
        }
        """

    @pytest.fixture
    def mutation_update_event(self):
        def _(event_id):
            return (
                """
                {
                    "query": "mutation NewEvent($date: DateTime, $id: String) {\
                        saveEvent(date: $date, eventId: $id) { new, event { date, location } }\
                    }",
                    "variables": {"date": "2018-09-02T01:07:03.112Z", "id": "%s"}
                }
                """
                % event_id
            )

        return _

    def test__mutation_save_event__authenticated__returns_query_data(
        self, user, mutation_new_event, snapshot
    ):
        token = create_access_token(user._id, fresh=True)
        url = url_for("graphql")
        res = self.client.post(
            url,
            headers={"Authorization": "Bearer {}".format(token)},
            content_type="application/json",
            data=mutation_new_event,
        )
        snapshot.assert_match(res.data)

    def test__mutation_save_event__not_authenticated__returns_errors(
        self, user, mutation_new_event, snapshot
    ):
        url = url_for("graphql")
        res = self.client.post(
            url, content_type="application/json", data=mutation_new_event
        )
        snapshot.assert_match(res.data)

    def test__mutation_save_event__given_id__updates_record(
        self, user, event, mutation_update_event, snapshot
    ):
        token = create_access_token(user._id, fresh=True)
        url = url_for("graphql")
        res = self.client.post(
            url,
            headers={"Authorization": "Bearer {}".format(token)},
            content_type="application/json",
            data=mutation_update_event(event._id),
        )
        snapshot.assert_match(res.data)
