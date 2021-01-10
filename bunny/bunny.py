#!/usr/bin/env python3
#
# Intialization of the package
#
# ----------------------------

# imports
# -------
import sshconf
from sshconf import empty_ssh_config_file

class CarrotNotFoundError(object):

    __version_error_parser__ = "0.0.1"
    __allow_update__ = False

    '''
    
    Raise any carrot errors for the bunny
    
    '''

    def __init__(self, message, errors):

        super().__init__(message)
        self.errors = errors

class Bunny(object):

    __version__ = '0.0.1'

    def __init__ (self, python_env, notebook_launch_command, port):

        '''

        Bunny Initialization for Proxy Jumping for servers

        '''

        self.empty_config_file = empty_ssh_config_file()
        self.path_to_python_env = python_env
        self.notebook_launch_command = notebook_launch_command
        self.port = str(port)
        self.hops = []
        self._config_file_path = ''

    def add_hop(self, name, hostname, user, proxy_jump = False):

        '''

        Add the hop to the bunny, essentially another port on the gateway.

        Arguments:
            name (String): name of the hop
            hostname (String): name of the host
            user (String): user for that host
            proxy_jump (Bool): The proxy jump server

        '''


        if proxy_jump:

            self.empty_config_file.add(
                name, Hostname=hostname, User=user, ProxyJump=self.hops[-1]['name'],
                Requesttty='force', LocalForward=self.port + ' 127.0.0.1:' + self.port,
                RemoteCommand=self.path_to_python_env + ' -m ' + self.notebook_launch_command + ' --port=' + self.port)

        else:
            self.empty_config_file.add(
                name, Hostname=hostname, User=user
            )

        self.hops.append({'name': name, 'hostname': hostname, 'user': user, 'proxy_jump': str(proxy_jump)})

    def generate_config(self):

        '''

        Generate the ssh config file

        '''

        import tempfile
        import os

        dirpath = tempfile.mkdtemp()
        self._config_file_path = os.path.join(dirpath + 'bunny_config')
        self.empty_config_file.write(self._config_file_path)
        print (dirpath)

    def run(self):

        '''

        Start the bunny - meaning to start the SSH command, read bunny_config, and launch the jupyter notebook

        '''

        import subprocess

        process =  subprocess.Popen('ssh -F ' + self._config_file_path + ' ' + self.hops[-1]['name'],
                                          shell=True,
                                          universal_newlines=True,
                                          stdin=subprocess.PIPE)
        process.wait()