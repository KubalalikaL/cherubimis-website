# nginx/Dockerfile

FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf
COPY certs/fullchain1.pem /etc/letsencrypt/live/cherubimis.stagging.whitehillscare.co.uk/fullchain.pem
COPY certs/privkey1.pem   /etc/letsencrypt/live/cherubimis.stagging.whitehillscare.co.uk/privkey.pem

