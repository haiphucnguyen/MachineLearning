#!/usr/bin/env bash

docker rm recommender
docker run --name recommender -d -it -p 5000:5000 -p 8888:8888 -v $PWD:/app ml:latest

docker exec -ti recommender sh -c "jupyter notebook list"
#docker exec -ti recommender sh -c "cd /app && uwsgi app.ini"