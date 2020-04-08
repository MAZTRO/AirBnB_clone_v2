#!/usr/bin/python3
"""
Script to compress and deploy a file
with Fabric into several servers
"""
from fabric.api import *
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
import os

env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


def deploy():
    path = do_pack()
    if (os.path.isfile(path)):
        dpld = do_deploy(path)
        return (dpld)
    return (False)
