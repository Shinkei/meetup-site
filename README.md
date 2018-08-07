# MEETUP SITE
---

This project is intended to be a self-hosted alternative to manage the
events of our community. But everyone is invited to use it and extend it
as desired.

## Table of Contents

- Features
- Installation
- Usage
- Contributing
- Credits
- License

## Features
- Log in with github OAuth
- Administrator privileges for members of the org
- Written in python and javascript
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
bin/compose dev exec api flask db upgrade # Run migrations on
development DB

bin/compose live exec api flask db upgrade # Run migrations on
production DB
```

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
bin/compose dev exec api pytest # Run tests on our backend
bin/compose dev exec ui yarn test # Run tests on our frontend
```
