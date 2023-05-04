#!/usr/bin/python3
""" Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean:
"""

from fabric.api import *
from datetime import datetime
from os.path import exists

# my web servers
env.hosts = ['54.165.42.62', '54.160.108.20']

def do_clean(number=0):
    """ deletes out-of-date archives
    """
    number = 1 if int(number) == 0 else int(number)
    # sort the achives in versions folder
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        # Delete all unnecessary archives
        [local("rm ./{}".format(a)) for a in archives]
    
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        # Delete all unnecessary archives
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
