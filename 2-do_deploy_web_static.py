#!/usr/bin/python3
""" distributes an archive to your web servers
using the function do_deploy """

from fabric.operations import local, put, run
from fabric.api import env
from datetime import datetime
from os import path

env.hosts = ['35.185.114.184', '34.75.131.28']


def do_pack():
    """ Function to generate the .tgz file """
    local("mkdir -p version")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                    capture=True)
    if archive.faile:
        return None
    return archive


def do_deploy(archive_path):
    """ Distributes an archive to the web servers """
    if not path.exists(archive_path):
        return False

    path_nx = path.splitext(archive_path)[0]
    path_nx = path_nx.split('/')[-1]
    path_yx = path_nx + '.tgz'

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{:s}/'.format(path_nx))
        run('tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}/'
            .format(path_yx, path_nx))
        run('rm /tmp/{:s}'.format(path_yx))
        run('mv /data/web_static/releases/{:s}/web_static/*'
            ' /data/web_static/releases/{:s}/'
            .format(path_nx, path_nx))
        run('rm -rf /data/web_static/releases/{:s}/web_static'.format(path_nx))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{:s}/ /data/web_static/current'
            .format(path_nx))
        print("New version deployed!")
        return True
    except:
        return False
