import graphene
import logging

from flask import request
from flask_graphql import GraphQLView
from flask_jwt_extended import verify_fresh_jwt_in_request, get_current_user
from graphene import relay
from graphql import GraphQLError

from .queries import UserQuery, EventQuery
from .mutations import EventMutation

logger = logging.getLogger(__name__)


class Query(UserQuery, EventQuery, graphene.ObjectType):
    node = relay.Node.Field()


class Mutation(EventMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


class EnhancedView(GraphQLView):
    def get_context(self):
        user = None
        try:
            verify_fresh_jwt_in_request()
            user = get_current_user()
        except Exception:
            logger.info("Failed to verify JWT")
        return {"request": request, "user": user}


class AuthorizationMiddleware(object):
    auth_not_required = set(["nextEvent"])  # fields that don't require authentication

    def resolve(self, next, root, info, **kwargs):
        if info.field_name not in self.auth_not_required:
            if not info.context.get("user"):
                raise GraphQLError("Authentication failed")
        return next(root, info, **kwargs)


def init_app(app):
    view = EnhancedView.as_view(
        "graphql",
        schema=schema,
        middleware=[AuthorizationMiddleware()],
        graphiql=app.config["DEBUG"],
    )
    app.add_url_rule("/graphql", view_func=view)
