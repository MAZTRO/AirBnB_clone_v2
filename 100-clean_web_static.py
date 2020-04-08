from fabric.api import *
from datetime import datetime
import os
""" Fabric script that deletes out-of-date archives"""
env.hosts = [
    "104.196.21.123",
    "54.226.145.255"
]
env.password = "MAZTRO"


def do_clean(number=0):
	local_path = "versions/"
	server_path = "/data/web_static/releases/"
	if (int(number) == 1 or int(number) == 0):
		local('find {} -type f -name "web_static_*" | sort -n | head -n -1 | xargs rm -f'.format(local_path))
		sudo('find {} -type d -name "web_static_*" | sort -n | head -n -1 | sudo xargs rm -rf'.format(server_path))
	elif (int(number) > 1):
		local('find versions/ -type f -name "web_static_*" | sort -n | head -n -{} | xargs rm -f'.format(number))
		sudo('find {} -type d -name "web_static_*" | sort -n | head -n -{} | sudo xargs rm -rf'.format(server_path, number))

	""" find versions/ -type f -name "web_static_*" | sort -n | head -n -2 | xargs rm -f """
	""" find versions/ -type d -name "web_static_*" | sort -n | head -n -2 | xargs rm -rf """
