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
        fls = archive_path.split("/")
        fld = fls[-1].split(".")
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}/".format(fld[0]))
        data = "/data/web_static/releases"
        sudo("tar -xzf /tmp/{} -C {}/{}/".format(fls[-1], data, fld[0]))
        sudo("rm /tmp/{}".format(fls[-1]))
        path_mv = "mv /data/web_static/releases"
        sudo("{}/{}/web_static/* {}/{}/".format(path_mv, fld[0], data, fld[0]))
        sudo("rm -rf {}/{}//web_static".format(data, fld[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/{}/ /data/web_static/current".format(data, fld[0]))
        print("New version deployed!")
        return True
    else:
        return False
