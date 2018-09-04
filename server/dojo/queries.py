import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import User as UserModel, Event as EventModel


class User(SQLAlchemyObjectType):
    is_admin = graphene.Boolean()

    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class UserCXN(relay.Connection):
    class Meta:
        node = User


class UserQuery(graphene.AbstractType):
    me = graphene.Field(User)
    all_users = SQLAlchemyConnectionField(UserCXN)

    def resolve_me(self, info):
        return info.context.get("user")


class Event(SQLAlchemyObjectType):
    location = graphene.List(graphene.Float)

    class Meta:
        model = EventModel
        interfaces = (relay.Node,)


class EventCXN(relay.Connection):
    class Meta:
        node = Event


class EventQuery(graphene.AbstractType):
    next_event = graphene.Field(Event)
    all_events = SQLAlchemyConnectionField(EventCXN)

    def resolve_next_event(self, info):
        pass
