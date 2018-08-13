#!/usr/bin/env sh

envsubst < /etc/ddclient/conf.template > /etc/ddclient/ddclient.conf

ddclient -daemon=1800

exec "$@"
