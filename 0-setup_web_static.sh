#!/usr/bin/env bash
# Script that sets up the web servers for the deployment of web_static.
STRING="\    location /hbnb_static {\n\
        alias /data/web_static/current;\n\
    }"
apt-get update -y
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "#Config file for NGINX server.

server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
    }
    error_page 404 /404.html;
}" > /etc/nginx/sites-available/default
service nginx restart
