#!/usr/bin/env bash

docker rm object-dt
docker run --name object-dt -it -d -p 8888:8888 -p 5000:5000 -v $PWD/notes:/home/jovyan/work -v $PWD/app:/app ml:latest

docker exec -ti object-dt sh -c "jupyter notebook list && cd /app && python main.py"
