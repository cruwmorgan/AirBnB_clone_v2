#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy:
 """

from fabric.api import *
from datetime import datetime
from os.path import exists

# my web servers
env.hosts = ['54.165.42.62', '54.160.108.20']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    req = local("sudo tar -cvzf {} web_static".format(filename))
    if req.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """script that distributes an archive to my web servers
    """
    # Returns False if the file at the path archive_path doesn’t exist
    if exists(archive_path) is False:
        return False
    # get the filename
    filename = archive_path.split('/')[-1]
    # archive to uncompress zip
    no_ext = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(no_ext))
        # Uncompress the archive to the folder /data/web_static/releases/
        # ...<archive filename without extension> on the web server
        run("tar -xzf {} -C {}/".format(tmp, no_ext))
        # Delete the archive from the web server
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_ext, no_ext))
        run("rm -rf {}/web_static".format(no_ext))
        # Delete the symbolic link /data/web_static/current from the server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link
        run("ln -s {}/ /data/web_static/current".format(no_ext))
        return True
    except archive_path.DoesNotExist:
        return False


def deploy():
    """ creates and distributes an archive to your web servers
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result
