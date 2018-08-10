from flask_graphql import GraphQLView
from flask_jwt_extended import fresh_jwt_required
import graphene
from graphene import relay

from .queries import UserQuery


class Query(UserQuery):
    node = relay.Node.Field()


schema = graphene.Schema(query=Query)


def init_app(app):
    view = GraphQLView.as_view("graphql", schema=schema, graphiql=app.config["DEBUG"])
    app.add_url_rule("/graphql", view_func=fresh_jwt_required(view))
