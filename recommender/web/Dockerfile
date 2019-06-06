FROM nginx:alpine

COPY dist/web /usr/share/nginx/html

#Build angular web command (in folder web):ng build
#Build imgage command: docker build -t recommender-web .
#Run docker command: docker run --name recommender-web -d -it -p 4200:80 -v $(pwd)/dist/web:/usr/share/nginx/html recommender-web
