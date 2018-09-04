from flask import (
    Blueprint,
    url_for,
    session,
    request,
    abort,
    render_template,
    current_app,
)
from flask_oauthlib.client import OAuth
from flask_jwt_extended import JWTManager, create_access_token
from .models import db, User, Organization

jwt = JWTManager()

oauth = OAuth()

github = oauth.remote_app("github", app_key="GH_OAUTH_CONFIG")

bp = Blueprint("login", __name__, url_prefix="/login")


@bp.route("")
def login():
    scheme = current_app.config["PREFERRED_URL_SCHEME"]
    url = url_for("login.authorized", _external=True, _scheme=scheme)
    return github.authorize(callback=url)


@bp.route("/authorized")
def authorized():
    response = github.authorized_response()
    token = response.get("access_token") if response else None
    if response is None or token is None:
        error_proxy = response or request.args
        return "Access denied: reason=%s error=%s resp=%s" % (
            error_proxy["error"],
            error_proxy["error_description"],
            error_proxy,
        )
    session["github_token"] = (token, "")

    user_id = _update_user_data()
    jwt = create_access_token(user_id, fresh=True)
    data = {"token": jwt, "domain": current_app.config["WEB_UI_URL"]}
    session.clear()
    return render_template("send_token.html", **data)


@github.tokengetter
def _get_github_oauth_token():
    return session.get("github_token")


@jwt.user_loader_callback_loader
def _load_user_from_token(user_id):
    return User.query.filter_by(_id=user_id).one_or_none()


def _update_user_data():
    user_data = github.get("user").data
    orgs_data = github.get("user/orgs").data
    orgs = [_update_or_create_org(data) for data in orgs_data]
    db.session.add_all(orgs)
    db.session.commit()
    user = _update_or_create_user(user_data, orgs)
    db.session.add(user)
    db.session.commit()
    return user._id


def _update_or_create_org(data):
    org = Organization.query.filter_by(import_id=data["id"]).one_or_none()
    if not org:
        org = Organization(import_id=data["id"])
    org.avatar_url = data["avatar_url"]
    org.handle = data["login"]
    return org


def _update_or_create_user(data, orgs):
    user = User.query.filter_by(import_id=data["id"]).one_or_none()
    if not user:
        user = User(import_id=data["id"])
    user.avatar_url = data["avatar_url"]
    user.profile_url = data["html_url"]
    user.handle = data["login"]
    user.name = data["name"]
    user.email = data["email"]
    user.orgs.clear()
    for org in orgs:
        user.orgs.append(org)
    return user
