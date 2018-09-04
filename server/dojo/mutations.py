import graphene
from sqlalchemy import exists

from dojo.models import db, Event as EventModel
from dojo.queries import Event as EventField


class SaveEvent(graphene.Mutation):
    class Input:
        event_id = graphene.String()
        date = graphene.types.datetime.DateTime()
        title_content = graphene.String()
        detail_title = graphene.String()
        detail_content = graphene.String()
        agenda_title = graphene.String()
        agenda_content = graphene.String()
        presenter_title = graphene.String()
        presenter_content = graphene.String()
        requirement_title = graphene.String()
        requirement_content = graphene.String()
        location = graphene.List(graphene.Float)

    new = graphene.Boolean()
    event = graphene.Field(EventField)

    @staticmethod
    def mutate(root, info, event_id=None, **kwargs):
        is_new = not (
            bool(event_id)
            and db.session.query(exists().where(EventModel._id == event_id)).scalar()
        )
        data = dict(kwargs, _id=event_id)
        event = (
            EventModel(**data)
            if is_new
            else EventModel.query.filter_by(_id=event_id).one()
        )
        if not is_new:
            for key in data:
                setattr(event, key, data[key])
        db.session.add(event)
        db.session.commit()
        return SaveEvent(new=is_new, event=event)


class EventMutation(graphene.AbstractType):
    save_event = SaveEvent.Field()
