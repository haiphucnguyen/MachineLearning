#!/usr/bin/env bash

docker run -p 8888:8888 --name jupyter -v $PWD/notes:/home/jovyan/work jupyter/tensorflow-notebook:abdb27a6dfbb

docker exec -ti jupyter sh -c "conda install -y swig && pip install pip install keras"