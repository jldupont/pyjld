#!/usr/bin/env python
"""
pyjld.phidgets.bonjour.daemon
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: bonjour_daemon.py 69 2009-04-17 18:49:17Z jeanlou.dupont $"

__all__ = ['PhidgetsBonjourDaemon',]

import signal
import sys
import time


from Phidgets.Phidget import *
from Phidgets.PhidgetException import *
from Phidgets.Manager import *

from pyjld.os.tools import safe_mkdir

#locals
from actions import Actions
from controller import controller_factory


class PhidgetsBonjourDaemon(object):
    """
    The daemon application
    """

    #_discoveredFolder="/var/phidgets"
    
    def __init__(self, logger_factory, messages):
        self.logger_factory = logger_factory
        self.logger = None
        self.name = "phidgets_bonjour"
        self.messages = messages
        
    def _initLogger(self):
        self.logger = self.logger_factory()
        
    def exit(self):
        self.logger.info("daemon exiting")
        
        
    def before_run(self):
        """
        Called before running the daemon
        """
        self._initLogger()
        
        
        # Phidget discovered folder
        """
        result, existed, path = self._preparePhidgetsDiscoveredFolder()
        if not result:
            self.logger.error("error_creating_phidgets_discovered_folder", 
                              path=path)
            return True

        if not existed:
            self.logger.info("info_created_phidgets_discovered_folder", path=path)
        """ 
            
        return False #don't abort
        
        
    def _preparePhidgetsDiscoveredFolder(self):
        """
        Creates the folder where discovered phidgets are recorded
        
        Note: not used at the moment.
        """

        try:
            existed, path = safe_mkdir(self._discoveredFolder)
        except:
            return False, False, None
        
        return True, existed, path
            
        
    def run(self):
        self.logger.info("daemon running")

        actions = Actions(self.logger)
        
        try:
            actions.createSessionBus()
            actions.createManager()
            actions.wireEventHandlers()
            actions.openManager()
            
            # MAIN LOOP
            # ---------        
            while True:
                #self.logger.info("start loop")
                
                try:
                    signal.pause()
                    #time.sleep(0.1)
                    #sys.stdin.read()
                except Exception,e:
                    exc=str(e)
                    self.logger.error("error_untrapped", exc=exc)
                    
                #self.logger.info("tail loop")
                
        except Exception,e:
            exc=str(e)
            self.logger.error("error_untrapped", exc=exc)
            
        return 0 # OK

