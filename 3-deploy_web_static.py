#!/usr/bin/python3
"""This module distributes the web_static content to two web servers.

Usage:
    This module uses Fabric to distribute the content, execute it like this:
    "fab -f 3-deploy_web_static.py deploy -i <private key path> -u <user>"
"""
from os import path
from fabric.api import env, put, run, local
from datetime import datetime

env.hosts = ['35.196.220.11', '35.196.58.181']


def deploy():
    """Call functions to pack and deploy the packed archive
    to web servers"""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder of
    your AirBnB Clone repo."""
    date_time = datetime.now()
    create_dir = local("mkdir -p versions")
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_time.year,
                                                              date_time.month,
                                                              date_time.day,
                                                              date_time.hour,
                                                              date_time.minute,
                                                              date_time.second)
    compress = local("tar -cvzf {} web_static".format(file_path))
    if create_dir.failed or compress.failed:
        return None
    return file_path


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
    if run("ln -sfn /data/web_static/releases/{}/ /data/web_static/current"
            .format(name)).failed:
        return False
    return True
