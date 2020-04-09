#!/usr/bin/env bash
# Configure a Server with Nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "** Holberton School **" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "43 a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
