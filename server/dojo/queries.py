import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class UserConnection(relay.Connection):
    class Meta:
        node = User


class UserQuery(graphene.ObjectType):
    me = graphene.Field(User)
    all_users = SQLAlchemyConnectionField(UserConnection)

    def resolve_me(self, info):
        return info.context.get("user")
