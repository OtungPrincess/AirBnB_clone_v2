#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
if ! type nginx &>/dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# recursively create directories
mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "created the test file" > /data/web_static/releases/test/index.html

ln -sf data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

sed -i "/server_name _;/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
