#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y install nginx
if [ ! -d /data ]
then;
	mkdir /data
	mkdir /data/web_static/releases/test/
	mkdir /data/web_static/shared/
fi
echo "Simple content to test my Nginx configuration" > /data/web_static/releases/test/index.html
if [ ! -f /data/web_static/releases/test/index.html]
then;
	rm /data/web_static/releases/test/index.html
	ln -s /data/web_static/current /data/web_static/releases/test/
else
	ln -s /data/web_static/current /data/web_static/releases/test/
fi
sudo chown -R ubuntu:ubuntu /data
sed -i '/^\tserver_name*/a\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
