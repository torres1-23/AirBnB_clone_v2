#!/usr/bin/python3
"""This module cleans old files.

Usage:
    This module uses Fabric to dclean the files, execute it like this:
    "fab -f 100-clean_web_static.py do_clean:number=<number to keep>
    -i <path to private key> -u <user_name>"
"""
import os
from fabric.api import local, run, env

env.hosts = ["35.196.220.11", "35.196.58.181"]


def do_clean(number=0):
    """Cleans out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    filenames = []
    local("ls -1 versions | sort -r > versionfiles")
    with open('versionfiles') as f:
        fileslines = f.read()
    for fileline in fileslines:
        if len(fileline) == 29 and fileline[:11] == "web_static_" and \
                          fileline[-4:] == ".tgz":
            filenames.append(fileline)
    if number < 2:
        if len(filenames) <= 1:
            return
        del_after_index = 1
    else:
        if number <= len(filenames):
            return
        del_after_index = number
    for i in range(del_after_index, len(filenames)):
        local("rm versions/{}".format(filenames[i]))
        run("rm -rf /data/web_static/releases/{}".format(filenames[i][:-4]))
