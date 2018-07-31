from flask import Flask
from .settings import Config
from .login import bp, oauth, jwt
from .models import db, migrate


def create_app(config=Config, **config_overrides):
    app = Flask(__name__)

    app.config.from_object(config)
    if config_overrides:
        app.config.update(config_overrides)

    @app.route("/health")
    def health():
        return "OK"

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    oauth.init_app(app)
    app.register_blueprint(bp)

    return app
