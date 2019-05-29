#!/usr/bin/env bash

docker run -p 8888:8888 -v $PWD/shared/notes:/home/jovyan/work jupyter/tensorflow-notebook:abdb27a6dfbb