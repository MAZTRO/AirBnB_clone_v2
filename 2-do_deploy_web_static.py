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

        push = put(archive_path, "/tmp/")
        new_dir = sudo("mkdir -p {}{}".format(pth_re, fld[0]))
        upk = sudo("{} /tmp/{} -C {}{}/".format(com, fls[-1], pth_re, fld[0]))
        rm_tgz = sudo("rm /tmp/{}".format(fls[-1]))
        mv_stc = sudo("mv {0}{1}/web_static/* {0}{1}".format(pth_re, fld[0]))
        rm_static = sudo("rm -rf {}{}/web_static".format(pth_re, fld[0]))
        rm_symb = sudo("rm -rf /data/web_static/current")
        do_symb = sudo("ln -s {}{}/ {}".format(pth_re, fld[0], pth_cur))
        print("New version deployed!")
        return True
    else:
        return False


"""
#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['35.231.167.55', '34.236.146.248']


def do_deploy(archive_path):
    if os.path.isfile(archive_path):
        path1 = archive_path.split("/")
        path2 = path1[-1].split(".")
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/release\
s/{}".format(path2[0]))
        sudo("tar -xzf /tmp/{} -C /data/web_static/release\
s/{}".format(path1[-1], path2[0]))
        sudo("rm /tmp/{}".format(path1[-1]))
        sudo("mv /data/web_static/releases/{0}/web_static/* /data/web_stat\
ic/releases/{0}/".format(path2[0]))
        sudo("rm -rf /data/web_static/releases/{}/web_stat\
ic/".format(path2[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_stat\
ic/current".format(path2[0]))
        print("New version deployed!")
        return True
    else:
        return False
"""