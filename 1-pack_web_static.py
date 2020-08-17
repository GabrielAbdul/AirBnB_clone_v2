#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents of the web_static folder'''
from datetime import datetime
from fabric.api import local


def do_pack():
    ''''''
    archive = 'web_static_{}.tgz'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
    local('mkdir -p versions')

    try:
        local('tar -cvzf versions/{} web_static'.format(archive))
        return "versions/{}".format(archive)
    except:
        return None
