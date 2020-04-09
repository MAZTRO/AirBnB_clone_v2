#!/usr/bin/python3
""" Script to deploy a compressed file with Fabric into several servers"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


def do_deploy(archive_path):
    if (os.path.isfile(archive_path)):
        com = "tar -xzf"
        pth_re = "/data/web_static/releases/"
        pth_cur = "/data/web_static/current"
        fls = archive_path.split("/")
        fld = fls[-1].split(".")

        put(archive_path, "/tmp/")
        sudo("mkdir -p {}{}".format(pth_re, fld[0]))
        sudo("{} /tmp/{} -C {}{}/".format(com, fls[-1], pth_re, fld[0]))
        sudo("rm /tmp/{}".format(fls[-1]))
        sudo("mv {0}{1}/web_static/* {0}{1}".format(pth_re, fld[0]))
        sudo("rm -rf {}{}/web_static".format(pth_re, fld[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}{}/ {}".format(pth_re, fld[0], pth_cur))

        print("New version deployed!")
        return True
    return False
