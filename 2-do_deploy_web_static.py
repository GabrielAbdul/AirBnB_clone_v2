#!/usr/bin/python3
'''Fabric script based on 1-pack_web_static.py'''
from fabric.api import run, put, env


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if not archive_path:
        return False
    try:
        # specify our servers
        web01, web02 = '104.196.165.127', '34.230.11.25'
        env.hosts = [web01, web02]
        # upload archive to tmp dir of both servers
        put(archive_path, '/tmp'/)
        # extract filename of file to perform op on
        file_name = run('ls -1')
        file_name = file_name.replace('.tgz', '')
        # decompress archive file
        run('tar -xzvf /tmp/{}'.file_name)
        # remove archive file
        run('rm {}.tgz'.format(archive_path))
        # remove old sym link
        run('rm /data/web_static/current')
        # create new one
        run('ln -sf /data/web_static/current /data/web_static/releases/{}'
            .format(file_name))
        return True
    except Exception:
        reuturn False
