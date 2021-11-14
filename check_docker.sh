#!/bin/bash -e

CHECK_VERSION=$1
REPO=$2

check=$(docker manifest inspect $REPO/godot:$CHECK_VERSION | grep 'no such manifest')
if [[ ${check} =~ *'no such manifest'* ]] ; then
    exit 0
else
    exit 1
fi
