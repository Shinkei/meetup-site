# MEETUP SITE

This project is intended to be a self-hosted alternative to manage the
events of our community. But everyone is invited to use it and extend it
as desired.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Log in with github OAuth
- Administrator privileges for members of the org
- Written in python and javascript
- ddclient included to update dynamic DNS
- Easy to use

## Installation

You can either run each component as you prefer or use the convenient
docker-compose files we provide.
[Here](https://docs.docker.com/compose/install/) you can find detailed
instructions to install docker-compose.

If you don't want to use docker-compose, you will need to have in your
system nodejs, python3, yarn, and pip, to manage dependencies which can
be found in [package.json](client/package.json) and
[requirements.txt](server/requirements.txt).

## Usage

Once you have docker-compose ready on your system, you can use it to
start the project. We have added a simple but convenient script to get
the system started in a few strokes of the keyboard.

```sh
bin/compose dev up # Will start the development server

bin/compose live up # Will start a production-ready server
```

After starting the server you need to run the migrations for all the DB
components to be created.

```sh
# Run migrations on development DB
bin/compose dev exec api flask db upgrade

# Run migrations on production DB
bin/compose live exec api flask db upgrade
```

### ENVIRONMENT VARIABLES

For the system to work as expected, some variables need to be set on
each of the following files:
- __live/.env__
  - `CERTBOT_EMAIL`
  - `DDCLIENT_WEB`
  - `DDCLIENT_PROTOCOL`
  - `DDCLIENT_SERVER`
  - `DDCLIENT_LOGIN`
  - `DDCLIENT_PASSWORD`
  - `DDCLIENT_DOMAIN`
  - `NGINX_HOST`
- __server/.env.live__
  - `GH_CONSUMER_KEY`
  - `GH_CONSUMER_SECRET`
  - `JWT_SECRET_KEY`
  - `SQLALCHEMY_DATABASE_URI`
  - `SERVER_NAME`
  - `WEB_UI_URL`
  - `PREFERRED_URL_SCHEME`
- __server/.env.dev__
  - `GH_CONSUMER_KEY`
  - `GH_CONSUMER_SECRET`
  - `JWT_SECRET_KEY`
  - `SQLALCHEMY_DATABASE_URI`
  - `SERVER_NAME`
  - `WEB_UI_URL`
  - `ENABLE_CORS`
- __client/.env.live__
  - `TITLE`
  - `API_BASE_URL`
- __client/.env.dev__
  - `TITLE`
  - `API_BASE_URL`

#### Description
- __API_BASE_URL__ should include protocol, and port if in dev environment
- __CERTBOT_EMAIL__ email for account notifications
- __DDCLIENT_DOMAIN__ domain to update
- __DDCLIENT_LOGIN__ to login on provider's server
- __DDCLIENT_PASSWORD__ to login on provider's server
- __DDCLIENT_PROTOCOL__ is the provider's update protocol
- __DDCLIENT_SERVER__ is the provider's server to update the record on
- __DDCLIENT_WEB__ is the provider's IP checking page
- __ENABLE_CORS__ enable CORS headers
- __GH_CONSUMER_KEY__ OAuth key for github's API
- __GH_CONSUMER_SECRET__ OAuth secret for github's API
- __JWT_SECRET_KEY__ key to sign the JWT with
- __NGINX_HOST__ domain name used to create certificates
- __PREFERRED_URL_SCHEME__ the default is http
- __SERVER_NAME__ should be the name and port number of the server
- __SQLALCHEMY_DATABASE_URI__ is the connection string to the database
- __TITLE__ is the what will be displayed in the UI
- __WEB_UI_URL__ is the full URL (including protocol) to access the UI

## Contributing

### Requesting features / Reporting bugs

Please browse the existing issues to see whether it has been previously
dicussed.
When reporting a bug it's important that you provide the full command
argument list as well as the output of the failing command and be as
descriptive as possible on how to reproduce the issue.

### Documenting

Documenting is a very important part of any project as it is a way of
communicating our findings, sharing our experiences, and making it
easier for everyone else. If you feel that something was not clear
enough or steps were omitted, please add them we will be very grateful.

### Coding

All of our code is formatted using
[standard](https://github.com/standard/standard) and
[black](https://github.com/ambv/black). Please make sure that your
changes conform to their rules.

Before opening a pull request, please make sure the test suite passes.
You should also add tests for any new features and bug fixes.

```sh
# Run tests on our backend
bin/compose dev exec api pytest

# Run tests on our frontend
bin/compose dev exec ui yarn test

# Run tests on our production stack
bin/compose live exec proxy bats tests
```

## License

Please see [LICENSE](LICENSE)
