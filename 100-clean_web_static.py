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
    if int(number) == 0:
        number = 1
    else:
        int(number)
    archives = sorted(os.listdir("versions"))
    for i in range(number):
        archives.pop()
    with lcd("versions"):
        for a in archives:
            local("rm ./{}".format(a))
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        for a in archives:
            if "web_static_" in a:
                archives = a
        for i in range(number):
            archives.pop()
        for a in archives:
            run("rm -rf ./{}".format(a))
