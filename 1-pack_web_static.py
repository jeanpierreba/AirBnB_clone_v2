#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack. """

from fabric.operations import local
from datetime import datetime


def do_pack():
    """ Function to generate the .tgz file """
    local("mkdir -p version")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                    capture=True)
    if archive.failed:
        return None
    return archive
