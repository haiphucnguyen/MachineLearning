#!/usr/bin/env bash

# docker build -t object-dt-web .
docker run --name object-dt-web -d -it -p 4200:80 -v $(pwd)/dist/web:/usr/share/nginx/html web

# start local: ng serve --proxy-config proxy.config.json
