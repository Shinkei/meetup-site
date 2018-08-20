#!/usr/bin/env bats

@test "the server is up" {
    curl -sI localhost:8080 | grep -q '200 OK'
}

@test "served content is protected from clickjacking" {
    curl -sI localhost:8080 | grep -q 'X-Frame-Options: SAMEORIGIN'
}

@test "health endpoint responds okay" {
    curl -sI localhost:8080 -H "Host: $NGINX_HOST" | grep -q '200 OK'
}
