#!/bin/bash

if [ "$STAGE" = "production" ] ; then
    docker run --detach=false --publish=8000:8000 -e STAGE=$STAGE {{ project_name }}:latest
else
    docker run --detach=false --publish=8000:8000 -e STAGE=$STAGE -v $(pwd)/app:/srv/app {{ project_name }}:dev
fi