#!/usr/bin/env bats

setup() {
    run curl -skI https://localhost:8443
    HEADERS=$output
}

@test "the server is up" {
    grep -q 'HTTP/1.1 200 OK' <<< $HEADERS
}

@test "served content is protected from clickjacking" {
    grep -q 'X-Frame-Options: SAMEORIGIN' <<< $HEADERS
}

@test "served content is protected from XSS" {
    grep -q 'X-XSS-Protection: 1; mode=block' <<< $HEADERS
}

@test "served content is protected from content-type sniffing" {
    grep -q 'X-Content-Type-Options: nosniff' <<< $HEADERS
}

@test "served content is protected from ssl stripping" {
    grep -q 'Strict-Transport-Security: max-age=31536000; includeSubdomains;' <<< $HEADERS
}

@test "health endpoint responds okay" {
    run curl -sk https://localhost:8443/health -H "Host: $NGINX_HOST"
    [ $output == 'OK' ]
}
