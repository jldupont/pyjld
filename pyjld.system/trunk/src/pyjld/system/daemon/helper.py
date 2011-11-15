#!/usr/bin/env python
"""
pyjld.system.daemon.helper

This module borrows heavily from python_daemon_ available at Pypi


.. _python_daemon: http://pypi.python.org/pypi/python-daemon/


@author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: helper.py 32 2009-04-02 17:13:57Z jeanlou.dupont $"

__all__ = ['PIDFileHelper', 'PIDFileHelperException', ]

import signal
import errno
import os

# not ideal I know but I develop on a Windows machine... for now
# ==============================================================
#from daemon.pidlockfile import PIDLockFile
try:    from daemon.pidlockfile import PIDLockFile
except: pass



class PIDFileHelperException(Exception):
    """
    PIDFileHelper Exception class
    
    Allows for easier translation of error messages.
    """
    def __init__(self, message, msg_id = None, params = None):
        Exception.__init__(self, message)
        self.msg_id = msg_id
        self.params = params
        
        


class PIDFileHelper(object):
    """ 
    PID file related helper functions
    """
    
    @classmethod
    def make_pidlockfile(cls, path):
        """ 
        Make a PIDLockFile instance with the given filesystem path. 
        """
        lockfile = None
    
        if path is not None:
            if not isinstance(path, basestring):
                raise PIDFileHelperException("Invalid filesystem path [%s]" % path, 
                                             msg_id="error_invalid_filesystem_path", 
                                             params={'path':path})

            if not os.path.isabs(path):
                raise PIDFileHelperException("Invalid absolute filesystem path [%s]" % path,
                                             msg_id= "error_invalid_absolute_path", 
                                             params= {'path':path})

            lockfile = PIDLockFile(path)
    
        return lockfile

    @classmethod    
    def pidfile_lock_is_stale(cls, pidfile):
        """ Determine whether a PID file refers to a nonexistent PID. """
        result = False
    
        pidfile_pid = pidfile.read_pid()
        try:
            os.kill(pidfile_pid, signal.SIG_DFL)
        except OSError, exc:
            if exc.errno == errno.ESRCH:
                # The specified PID does not exist
                result = True
    
        return result
    
