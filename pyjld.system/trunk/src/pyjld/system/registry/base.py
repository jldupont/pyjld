""" 
pyjld.system.registry.base
"""
__author__  = "Jean-Lou Dupont"
__fileid    = "$Id: base.py 37 2009-04-03 01:58:16Z jeanlou.dupont $"

__all__ = ['Registry', 'RegistryException']

import sys

class RegistryException(Exception):
    """ 
    An exception class for Registry
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)



class Registry(object):
    """
    Facade for the cross-platform Registry
    
    Can be accessed like a dictionary: for this
    functionality, an instance must be constructed
    with the 'file' parameter specified.
    """
    reg = None
    
    def __init__(self, file = None):
        self.file = file
        
        if sys.platform[:3] == 'win':
            from pyjld.system.registry.reg_windows import WindowsRegistry 
            self.reg = WindowsRegistry(file)
        else:
            from pyjld.system.registry.reg_linux import LinuxRegistry
            self.reg = LinuxRegistry(file)
    
    def getKey(self, file, key):
        """
        GETS the specified key
        """
        return self.reg.getKey(file, key)
    
    def setKey(self, file, key, value, cond = False):
        """
        SETS the specified key
        """
        if (cond):
            if (value is None):
                #print "skipping key[%s]" % key
                return
        return self.reg.setKey(file, key, value)
    
    # DICTIONARY INTERFACE
    # ====================
    
    def __getitem__(self, key):
        return self.reg.get(key, None)
    
    def __setitem__(self, key, value):
        self.reg[key] = value
    
    def __contains__(self, key):
        return (key in self.reg)
        
