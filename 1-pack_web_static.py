#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack. """

from fabric.operations import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
