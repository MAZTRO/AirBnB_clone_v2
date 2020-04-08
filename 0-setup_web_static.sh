#!/usr/bin/env bash
# Configure a Server with Nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    ** Holberton School ** \n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "s/root \/var\/www\/html;/root \/data\/web_static\/current\/;/g" /etc/nginx/sites-enabled/default
sed -i "/root \/data\/web_static\/current\/;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
