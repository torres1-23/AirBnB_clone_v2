#!/usr/bin/python3
"""This module distributes the web_static content to two web servers.

Usage:
    This module uses Fabric to distribute the content, execute it like this:
    "fab -f 2-do_deploy_web_static.py do_deploy:<path to archive>
     -i <private key path> -u <user>"
"""
from os import path
from fabric.api import env, put, run
from datetime import datetime

env.hosts = ['35.196.220.11', '35.196.58.181']


def do_deploy(archive_path):
    """Deploys a .tgz file to web servers.

    Args:
        archive_path(string): Path to archive.
    """
    if path.exists(archive_path) is False:
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False
    if (run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name)).failed):
        return False
    if run("rm -rf /tmp/{}".format(file_name)).failed:
        return False
    if (run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(name, name)).failed):
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name)).failed:
        return False
    return True
