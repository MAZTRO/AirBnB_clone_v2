#!/usr/bin/python3
"""
Script to compress and deploy a file
with Fabric into several servers
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


@runs_once
def do_pack():
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    name = "web_static_{}.tgz".format(time)

    # local('mkdir -p versions')
    print("Packing web_static to versions/{}".format(name))
    command = "mkdir -p versions && tar -cvzf"
    output = local('{} versions/{} web_static'.format(command, name))
    if (output.succeeded):
        size = os.path.getsize("versions/{}".format(name))
        print("web_static packed: versions/{} -> {}Bytes".format(name, size))
        print("")
        return ("versions/{}".format(name))
    return ("None")


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


@task
def deploy():
    path = do_pack()
    if (os.path.isfile(path)):
        dpld = do_deploy(path)
        return (dpld)
    else:
        return (False)
