""" 
Windows Registry
"""
__author__  = "Jean-Lou Dupont"
__fileid    = "$Id: reg_windows.py 37 2009-04-03 01:58:16Z jeanlou.dupont $"

import sys
import _winreg

from pyjld.system.registry import RegistryException

class WindowsRegistry(object):
    
    _win = "Software\\Python\\Registry\\%s"

    def __init__(self, file = None):
        self.file = file

    def __getitem__(self, key):
        if (self.file is None):
            raise Exception('file property must be set to use the dict interface')        
        return self.getKey(self.file, key)
        
    def __setitem__(self, key, value):
        if (self.file is None):
            raise Exception('file property must be set to use the dict interface')        
        return self.setKey(self.file, key, value)
        
    def __contains__(self, key):
        if (self.file is None):
            raise Exception('file property must be set to use the dict interface')        
        return (self.getKey(self.file, key) is not None)

    def getKey(self, file, key):

        result = None
        subkey = self._win % file
        try:
            rkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, subkey, 0, _winreg.KEY_READ)
            (value, valuetype) = _winreg.QueryValueEx(rkey, key)
            result = value
        except:
            pass
        
        return result

    def setKey(self, file, key, value):
        try:
            #print "writing registry: key[%s] val[%s]" % (key,value)
            subkey = self._win % file
            ckey = _winreg.CreateKey( _winreg.HKEY_LOCAL_MACHINE, subkey)
            _winreg.SetValueEx(ckey, key, 0, _winreg.REG_SZ, value)           
        except Exception,e:
            raise RegistryException("Python Registry: write error key[%s] file[%s] exception msg{%s}" % (key, file, e))
        
