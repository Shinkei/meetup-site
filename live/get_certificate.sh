#!/usr/bin/env sh

CUSTOM_ARGS="--http-01-port 8080 --domains $NGINX_HOST --email $CERTBOT_EMAIl"
certbot --nginx certonly --non-interactive --agree-tos $CUSTOM_ARGS --keep
