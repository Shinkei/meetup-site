#!/usr/bin/env sh

pip install --user gunicorn==19.9.0

exec "$@"
