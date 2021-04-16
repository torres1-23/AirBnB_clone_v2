#!/usr/bin/python3
"""This module cleans old files.

Usage:
    This module uses Fabric to dclean the files, execute it like this:
    "fab -f 100-clean_web_static.py do_clean:number=<number to keep>
    -i <path to private key> -u <user_name>"
"""
import os
from fabric.api import local, run, env, cd, lcd

env.hosts = ["35.196.220.11", "35.196.58.181"]


def do_clean(number=0):
    """Cleans out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    try:
        number = int(number)
    except:
        return None
    if number < 0:
        return None
    if (number is 0 or number is 1):
        number = 2
    else:
        number += 1
    r_path = "/data/web_static/releases/"
    l_path = "./versions"
    with lcd(l_path):
        local('ls -t | tail -n +{} | xargs rm -rf --'.
              format(number))
    with cd(r_path):
        run('ls -t | tail -n +{} | xargs rm -rf --'.
            format(number))
