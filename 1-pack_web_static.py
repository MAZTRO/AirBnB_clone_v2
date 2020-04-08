#!/usr/bin/python3
""" Script to create a compressed file with Fabric """
from fabric.api import *
from datetime import datetime
import os

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
