#!/usr/bin/python3
'''Fabric script based on 1-pack_web_static.py'''
from fabric.api import run, put, env


# specify our servers
web01, web02 = '104.196.165.127', '34.230.11.25'
env.hosts = [web01, web02]


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if not archive_path:
        return False
    try:
        # upload archive to tmp dir of both servers
        put(archive_path, '/tmp/')
        # extract filename of file to perform op on
        file_name_ext = archive_path.split('/')[1]
        file_name = file_name_ext.split('.')[0]
        # create destination var
        run('mkdir -p /data/web_static/releases/{}/'.format(file_name))
        # decompress archive file
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name_ext, file_name))
        # remove archive file
        run('rm -rf /tmp/{}'.format(file_name_ext))
        # move files
        p = '/data/web_static/releases'
        run('mv {}/{}/web_static/* {}/{}'.format(p, file_name, p, file_name))
        # remove old sym link
        run('rm -rf /data/web_static/current')
        # create new one
        run('ln -s /data/web_static/releases/{}/\
            /data/web_static/current'.format(file_name))
        print('New version deployed!')
        return True
    except Exception:
        return False
