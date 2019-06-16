#!/usr/bin/env bash

docker rm object-dt
docker run --name object-dt -it -p 8888:8888 -v $PWD/notes:/home/jovyan/work ml:latest