import os


class Config(object):
    SERVER_NAME = os.environ.get("SERVER_NAME")
    PREFERRED_URL_SCHEME = os.environ.get("PREFERRED_URL_SCHEME", "http")
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    GH_OAUTH_CONFIG = dict(
        consumer_key=os.environ.get("GH_CONSUMER_KEY"),
        consumer_secret=os.environ.get("GH_CONSUMER_SECRET"),
        request_token_params={"scope": "read:user,read:org"},
        base_url="https://api.github.com/",
        request_token_url=None,
        access_token_method="POST",
        access_token_url="https://github.com/login/oauth/access_token",
        authorize_url="https://github.com/login/oauth/authorize",
    )
    GH_ORG_ID = os.environ.get("GH_ORG_ID")
    WEB_UI_URL = os.environ.get("WEB_UI_URL")
    JWT_IDENTITY_CLAIM = "sub"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENABLE_CORS = os.getenv("ENABLE_CORS", "0") == "1"
