#!/usr/bin/env bats

ARGS="--nginx certonly --http-01-port 8080 --domains $NGINX_HOST --non-interactive --agree-tos --email $CERTBOT_EMAIL"

@test "certificates can be generated" {
    run certbot --dry-run --staging $ARGS
    [ "$status -eq 0" ]
    grep -q 'The dry run was successful' <<< $output
}
