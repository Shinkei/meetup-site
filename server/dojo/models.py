from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
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


class User(db.Model, Base):
    __tablename__ = "users"

    id = db.Column(UUID, server_default=db.text("uuid_generate_v4()"), primary_key=True)
    import_id = db.Column(db.Integer, index=True)
    avatar_url = db.Column(db.String)
    profile_url = db.Column(db.String)
    handle = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)

    orgs = relationship("Organization", secondary=users_orgs, backref="users")


class Organization(db.Model, Base):
    __tablename__ = "organizations"

    id = db.Column(UUID, server_default=db.text("uuid_generate_v4()"), primary_key=True)
    import_id = db.Column(db.Integer, index=True)
    avatar_url = db.Column(db.String)
    handle = db.Column(db.String)
