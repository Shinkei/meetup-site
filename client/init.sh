#!/usr/bin/env sh

cd /home/node/app
[ ! -L $PWD/node_modules ] && ln -s /tmp/node_modules

exec "$@"
