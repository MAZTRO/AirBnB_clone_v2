#!/usr/bin/python3
""" Script to deploy a compressed file with Fabric into several servers"""
from fabric.api import *
from datetime import datetime
import os.path

env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


def do_deploy(archive_path):
    if os.path.isfile(archive_path):
        file = archive_path.split("/")
        pt = file[-1].split(".")
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/\
{}".format(pt[0]))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/\
{}".format(file[-1], pt[0]))
        sudo("rm /tmp/{}".format(file[-1]))
        sudo("mv /data/web_static/releases/{0}/web_static/* \
/data/web_static/releases/{0}/".format(path2[0]))
        sudo("rm -rf \
/data/web_static/releases/{}/web_static/".format(pt[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} \
/data/web_static/current".format(pt[0]))
        print("New version deployed!")
        return True
    else:
        return False
