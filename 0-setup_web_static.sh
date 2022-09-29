#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
if ! type nginx 2>/dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

if [[ ! -d data ]]
then
    mkdir data
fi

if [[ ! -d data/web_static ]]
then
    mkdir data/web_static
fi

if [[ ! -d data/web_static/releases ]]
then
    mkdir data/web_static/releases
fi

if [[ ! -d data/web_static/shared ]]
then
    mkdir data/web_static/shared
fi

if [[ ! -d data/web_static/releases/test ]]
then
    mkdir data/web_static/releases/test
fi

echo "created the test file" > data/web_static/releases/test/index.html


symlink=data/web_static/current
if [[ -L $symlink ]]
then
    rm $symlink
fi

ln -s data/web_static/releases/test/ $symlink

# returns an id if user is present
if ! id -u ubuntu &>/dev/null
then
    useradd ubuntu
fi

chown -R ubuntu data/
chgrp -R ubuntu data/

sed -i "/server_name _;/a \\\n\tlocation /hbnb_static {\n\t\talias data/web_static/current;\n\t}" /etc/nginx/sites-available/default
