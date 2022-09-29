#!/usr/bin/python3
"""
    This script creates and distributes an archive to your web servers,
    using the function deploy
"""
from fabric.api import *
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


env.user = 'ubuntu'
env.hosts = ['44.210.77.98', '44.211.31.180']


def deploy():
    """
        packs and deploys web_static
    """
    archived = do_pack()
    if not archived:
        return False

    return do_deploy(archived)
