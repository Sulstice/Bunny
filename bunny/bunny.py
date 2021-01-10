#!/usr/bin/env python3
#
# Intialization of the package
#
# ----------------------------


# imports
# -------
import sshconf

class CarrotNotFoundError(object):

    __version_error_parser__ = "1.1.0"
    __allow_update__ = False

    '''
    
    Raise any carrot errors for the bunny
    '''

    def __init__(self, message, errors):

        super().__init__(message)
        self.errors = errors

class Bunny(object):

    __version__ = '0.1.0'

    def __init__ (self):



if __name__ == '__main__':

    bunny = Bunny()
