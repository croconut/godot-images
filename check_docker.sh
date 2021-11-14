#!/bin/bash -e

CHECK_VERSION=$1
REPO=$2

set +e
docker manifest inspect $REPO/godot:$CHECK_VERSION > /dev/null 2>&1 
exit_code="$?"
set -e
if [[ "$exit_code" != '0' ]] ; then
    exit 0
else
    exit 1
fi
