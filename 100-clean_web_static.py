#!/usr/bin/python3
""" Fabric script that deletes out-of-date archives"""
from fabric.api import *

env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


def do_clean(number=0):
    local_path = "versions/"
    server_path = "/data/web_static/releases/"
    grep = " | grep -v test | sort | uniq -u | sudo xargs rm -rf"

    if (int(number) == 1 or int(number) == 0):
        number = 1
        local("(ls -rt {} | head -n -{}){}".format(local_path, number, grep))
        sudo("(ls -rt {} | head -n -{}){}".format(server_path, number, grep))
    elif (int(number) > 1):
        local("(ls -rt {} | head -n -{}){}".format(local_path, number, grep))
        sudo("(ls -rt {} | head -n -{}){}".format(server_path, number, grep))
