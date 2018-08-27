#!/usr/bin/env bats

@test "the DNS can be updated" {
    ddclient -daemon=0 -debug -verbose -noquiet | grep -q 'SUCCESS'
}
