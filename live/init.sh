#!/usr/bin/env sh

envsubst < /etc/ddclient/conf.template > /etc/ddclient/ddclient.conf

ddclient -daemon=1800

SSL_NGINX_CONF=/etc/letsencrypt/options-ssl-nginx.conf
if [ ! -f $SSL_NGINX_CONF ]; then
    CUSTOM_ARGS="--http-01-port 8080 --domains $NGINX_HOST --email $CERTBOT_EMAIl"
    certbot --nginx certonly --non-interactive --agree-tos $CUSTOM_ARGS
fi

exec "$@"
