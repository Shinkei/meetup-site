import json

from flask import current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.elements import WKTElement
from geoalchemy2.functions import ST_AsGeoJSON
from geoalchemy2.types import Geometry
from osgeo import ogr
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship


db = SQLAlchemy()

migrate = Migrate()


class Base:
    __iter__ = lambda self: iter(
        [(x.key, str(getattr(self, x.key))) for x in inspect(self).attrs]
    )


users_orgs = db.Table(
    "user_organization_mappings",
    db.Column("user_id", UUID, db.ForeignKey("users.id"), primary_key=True),
    db.Column("org_id", UUID, db.ForeignKey("organizations.id"), primary_key=True),
)


events_users = db.Table(
    "event_user_mappings",
    db.Column("user_id", UUID, db.ForeignKey("users.id"), primary_key=True),
    db.Column("event_id", UUID, db.ForeignKey("events.id"), primary_key=True),
)


class User(db.Model, Base):
    __tablename__ = "users"

    _id = db.Column(
        "id", UUID, server_default=db.text("uuid_generate_v4()"), primary_key=True
    )
    import_id = db.Column(db.Integer, index=True, nullable=False)
    avatar_url = db.Column(db.String)
    profile_url = db.Column(db.String)
    handle = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)

    orgs = relationship("Organization", secondary=users_orgs, backref="users")

    @hybrid_property
    def is_admin(self):
        return any(
            org.import_id == current_app.config.get("GH_ORG_ID") for org in self.orgs
        )


class Organization(db.Model, Base):
    __tablename__ = "organizations"

    _id = db.Column(
        "id", UUID, server_default=db.text("uuid_generate_v4()"), primary_key=True
    )
    import_id = db.Column(db.Integer, index=True, nullable=False)
    avatar_url = db.Column(db.String)
    handle = db.Column(db.String)


class Event(db.Model, Base):
    __tablename__ = "events"

    _id = db.Column(
        "id", UUID, server_default=db.text("uuid_generate_v4()"), primary_key=True
    )
    date = db.Column(db.DateTime, index=True, nullable=False)
    _location = db.Column("location", Geometry(geometry_type="POINT", srid=4326))
    title_content = db.Column(db.String)
    description_title = db.Column(db.String)
    description_content = db.Column(db.String)
    agenda_title = db.Column(db.String)
    agenda_content = db.Column(db.String)
    presenter_title = db.Column(db.String)
    presenter_content = db.Column(db.String)
    requirement_title = db.Column(db.String)
    requirement_content = db.Column(db.String)

    attendees = relationship("User", secondary=events_users, backref="events")

    @hybrid_property
    def location(self):
        #json_str = db.session.query(ST_AsGeoJSON(self._location)).scalar()
        #if not json_str:
        #    return []
        #data = json.loads(json_str)
        #return data["coordinates"]
        point = ogr.CreateGeometryFromWkb(self._location)
        return [point.GetX(), point.GetY()]

    @location.setter
    def location(self, pair):
        # pair should be ordered [lon, lat]
        self._location = WKTElement("POINT(%f %f)" % tuple(pair), srid=4326)
