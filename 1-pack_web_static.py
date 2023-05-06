#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import *
from datetime import datetime
import os

# generates archive
def do_pack():
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    req = local("sudo tar -cvzf {} web_static".format(filename))
    if req.succeeded:
        os.chmod(filename, 0o664)
        return filename
    else:
        return None
