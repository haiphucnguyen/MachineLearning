#!/usr/bin/env bash

# docker build -t recommender-web .
docker run --name recommender-web -d -it -p 4200:80 -v $(pwd)/dist/web:/usr/share/nginx/html recommender-web
