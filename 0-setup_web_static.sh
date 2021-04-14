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
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^    server_name .*/a $STRING" /etc/nginx/sites-available/default
service nginx restart
