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
    """ deploy a file """
    if (os.path.isfile(archive_path)):
        p1 = archive_path.split("/")
        # ['versions', 'web_static_20170315003959.tgz']
        p2 = p1[-1].split(".")
        # ['web_static_20170315003959', 'tgz']
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}/".format(p2[0]))
        data = "/data/web_static/releases"
        sudo("tar -xzf /tmp/{} -C {}/{}/".format(p1[-1], data, p2[0]))
        sudo("rm /tmp/{}".format(p1[-1]))
        path = "mv /data/web_static/releases"
        path2 = "/data/web_static/releases"
        sudo("{}/{}/web_static/* {}/{}/".format(path, p2[0], path2, p2[0]))
        sudo("rm -rf {}/{}//web_static".format(path2, p2[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/{}/ /data/web_static/current".format(path2, p2[0]))
        print("New version deployed!")
        return True
    else:
        return False
