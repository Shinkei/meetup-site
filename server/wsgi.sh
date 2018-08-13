#!/usr/bin/env sh

gunicorn --bind 0.0.0.0:8080 -w 4 "dojo:create_app()"
