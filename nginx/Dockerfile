# nginx/Dockerfile

FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf
COPY certs/fullchain1.pem /etc/letsencrypt/live/cherubimis.com/fullchain.pem
COPY certs/privkey1.pem   /etc/letsencrypt/live/cherubimis.com/privkey.pem

