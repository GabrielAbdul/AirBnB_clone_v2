#!/usr/bin/python3
'''Fabric script that'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''generates a tgz archive'''
    archive = 'web_static_{}.tgz'.format(datetime.now().strftime
                                         ('%Y%m%d%H%M%S'))
    local('mkdir -p versions')

    try:
        local('tar -cvzf versions/{} web_static'.format(archive))
        return "versions/{}".format(archive)
    except:
        return None
