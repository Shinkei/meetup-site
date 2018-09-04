import pytest
import re

from sqlalchemy import create_engine

from dojo import create_app
from dojo.models import db, User, Organization, Event
from dojo.settings import Config


ADMIN_ORG_ID = 999


@pytest.fixture(scope="session", autouse=True)
def app(create_db):
    db_uri = re.sub(r"/[^/]+$", "/testing", Config.SQLALCHEMY_DATABASE_URI)
    app = create_app(
        SQLALCHEMY_DATABASE_URI=db_uri,
        SERVER_NAME="test.local",
        GH_ORG_ID=ADMIN_ORG_ID,
        TESTING=True,
    )

    ctx = app.app_context()
    ctx.push()
    db.session.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    db.session.execute('CREATE EXTENSION IF NOT EXISTS "postgis"')
    db.session.execute("COMMIT")
    db.create_all()
    yield app
    ctx.pop()


@pytest.fixture(scope="session")
def create_db():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    conn = engine.connect()
    conn.execute("COMMIT")
    conn.execute("DROP DATABASE IF EXISTS testing")
    conn.execute("COMMIT")
    conn.execute("CREATE DATABASE testing")
    conn.close()


@pytest.fixture(scope="function")
def session(request):
    connection = db.engine.connect()
    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)
    db.session = session

    transaction = connection.begin()

    def teardown():
        transcation.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)


@pytest.fixture(scope="function")
def user():
    u = User(name="Foo Bar", avatar_url="...img", import_id=123)
    db.session.add(u)
    db.session.commit()
    return u


@pytest.fixture(scope="function")
def admin_org():
    o = Organization(handle="adminorg", import_id=ADMIN_ORG_ID)
    db.session.add(o)
    db.session.commit()
    return o


@pytest.fixture(scope="function")
def make_admin(admin_org):
    def _(u):
        u.orgs.append(admin_org)
        db.session.add(u)
        db.session.commit()

    return _


@pytest.fixture(scope="function")
def event():
    lon = -75.5361111
    lat = 6.2913889
    e = Event(date="2018-09-01T11:00:00", location=[lon, lat])
    db.session.add(e)
    db.session.commit()
    return e
