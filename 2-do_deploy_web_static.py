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
        """ sudo("sudo chown -R ubuntu:ubuntu /data/") """
        print("New version deployed!")

        commands = [push,
                    new_dir,
                    upk,
                    rm_tgz,
                    mv_stc,
                    rm_static,
                    rm_symb,
                    do_symb
                    ]
        res = all(operation.succeeded for operation in commands)
        return(res)
    return False
