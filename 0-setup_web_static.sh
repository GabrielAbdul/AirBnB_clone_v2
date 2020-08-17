#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y install nginx
mkdir -p /data
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Simple content to test my Nginx configuration" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed -i '/^\tserver_name*/a\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
