#!/usr/bin/env bash
set -e

run() {
    if [[ $1 =~ .*\.(swift)$ ]]; then
        swiftlint lint --fix --format "$1"
    fi
}

task() {
    foreach_changed_file run
}
