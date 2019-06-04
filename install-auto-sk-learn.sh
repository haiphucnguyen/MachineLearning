#!/usr/bin/env bash

docker exec -ti jupyter sh -c "conda install -y swig && pip install -r /home/jovyan/work/auto-sklearn-requirements.txt && pip install tpot"