from fabric.api import *
from datetime import datetime
import os
""" Fabric script that deletes out-of-date archives"""
env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


def do_clean(number=0):
    local_path = "versions/"
    server_path = "/data/web_static/releases/"
    local_name = '-type f -name "web_static_*"'
    server_name = '-type d -name "web_static_*"'
    local_pipe = "| sort -n | head -n -1 | xargs rm -f"
    server_pipe = "| sort -n | head -n -1 | sudo xargs rm -rf"

    if (int(number) == 1 or int(number) == 0):
        local('find {} {} {}'.format(local_path, local_name, local_pipe))
        sudo('find {} {} {}'.format(server_path, server_name, server_pipe))
    elif (int(number) > 1):
        local('find {} {} | sort -n | head -n -{} | \
xargs rm -f'.format(local_path, local_name, number))
        sudo('find {} {} | sort -n | head -n -{} | \
sudo xargs rm -rf'.format(server_path, server_name, number))
