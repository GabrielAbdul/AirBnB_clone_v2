#!/usr/bin/python3
'''Fabric script based on 2-do_deploy_web_static.py'''

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

web01, web02 = '104.196.165.127', '34.230.11.25'
env.hosts = [web01, web02]

def deploy():
    '''creates and distributes an archive to web servers'''
    path_name = do_pack()
    if not path_name:
        return False
    return(do_deploy(path_name))
