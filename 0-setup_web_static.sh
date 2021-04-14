#!/usr/bin/env bash
#
STRING='\    location /hbnb_static {\
        alias /data/web_static/current;\
    }'
apt-get update -y
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^    server_name .*/a $STRING" /etc/nginx/sites-available/default
service nginx restart
