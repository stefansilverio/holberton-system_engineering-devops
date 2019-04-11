#!/usr/bin/python3
"""compress files"""
from fabric.api import local, run, put, env

env.key_filename = '~/.ssh/holberton'
env.user = 'ubuntu'

def pack():
    """create tarball of cwd"""
    local("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")

def deploy():
    """upload archive file"""
    put("holbertonwebapp.tar.gz", "/tmp/")
    run("mkdir /tmp/holbertonwebapp")
    run("tar xzf /tmp/holbertonwebapp.tar.gz -C /tmp/holbertonwebapp")

def clean():
    """clean tar file on local"""
    local("rm -rf holbertonwebapp.tar.gz")
