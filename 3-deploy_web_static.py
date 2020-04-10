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
    """ deploy a file """
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
        sudo("ln -s {}{} {}".format(pth_re, fld[0], pth_cur))
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
    return (False)
