import pytest
import re

from sqlalchemy import create_engine

from dojo import create_app
from dojo.models import db, User
from dojo.settings import Config


@pytest.fixture(scope="session", autouse=True)
def app(create_db):
    db_uri = re.sub(r"/[^/]+$", "/testing", Config.SQLALCHEMY_DATABASE_URI)
    app = create_app(
        SQLALCHEMY_DATABASE_URI=db_uri, SERVER_NAME="test.local", TESTING=True
    )

    ctx = app.app_context()
    ctx.push()
    db.session.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
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
    u = User(name="Foo Bar", avatar_url="...img")
    db.session.add(u)
    db.session.commit()
    return u
