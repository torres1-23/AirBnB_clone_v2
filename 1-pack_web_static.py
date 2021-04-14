#!/usr/bin/python3
"""This module compress the web_static directory.

Usage:
    This module uses Fabric to create a tarball of all the static content
    of a website, execute like this:
    "fab -f 1-pack_web_static.py do_pack"
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder of
    your AirBnB Clone repo."""
    date_time = datetime.now()
    create_dir = local("mkdir -p versions", capture=True)
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_time.year,
                                                              date_time.month,
                                                              date_time.day,
                                                              date_time.hour,
                                                              date_time.minute,
                                                              date_time.second)
    compress = local("tar -cvf {} web_static".format(file_path))
    if create_dir.failed or compress.failed:
        return None
    return file_path
