import graphene
import logging

from flask import request
from flask_graphql import GraphQLView
from flask_jwt_extended import verify_fresh_jwt_in_request, get_current_user
from graphene import relay

from .queries import UserQuery

logger = logging.getLogger(__name__)


class Query(UserQuery):
    node = relay.Node.Field()


schema = graphene.Schema(query=Query)


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
    auth_required = ["node", "me", "all_users"]

    def resolve(self, next, root, info, **args):
        if info.field_name in self.auth_required:
            assert info.context.get("user"), "Authentication failed"
        return next(root, info, **args)


def init_app(app):
    view = EnhancedView.as_view(
        "graphql",
        schema=schema,
        middleware=[AuthorizationMiddleware()],
        graphiql=app.config["DEBUG"],
    )
    app.add_url_rule("/graphql", view_func=view)
