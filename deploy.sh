#!/bin/bash

docker build -t 'recipe-app' -f 'Dockerfile' .
TAG=$(date +%s) # timestamp
docker tag recipe-app luthfihrz/recipe-app-poc:$TAG
docker push luthfihrz/recipe-app-poc:$TAG

# MANTAAP!