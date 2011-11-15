#!/usr/bin/env python
"""
pyjld.phidgets.erl_manager.actions
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: actions.py 70 2009-04-20 13:46:19Z jeanlou.dupont $"

__all__ = ['Actions',]


from Phidgets.Phidget import *
from Phidgets.PhidgetException import *
from Phidgets.Manager import *

from pyjld.system.proxy import ProxyCallback


class ActionsError(Exception):
    def __init__(self, msg_id, params=None):
        Exception.__init__(self, msg_id)
        self.msg_id = msg_id
        self.params = params




class Actions(object):
    """
    Actions for the Controller
    
    - Create an instance of this class with a logger
    - Use createManager
    - Use wireEvents(controller)
    - Use openManager
    
    Periodically, perform testManager

    """
    
    
    def __init__(self, logger):
        self.manager = None
        self.logger = logger
          
    
    def createManager(self):
        """
        Builds a Phidget Manager
        
        :rtype: boolean, result of Manager creation
        """
        try:
            self.manager = Manager()
            return True
        except Exception,e:
            self.logger.error("error_creating_phidgets_manager")
        
        self.manager = None
        return False
    
    def wireEventHandlers(self):
        
        try:
            self.manager.setOnAttachHandler(self.doAttach)
            self.manager.setOnDetachHandler(self.doDetach)
            #self.manager.setOnErrorHandler(self.doError)
        except Exception,e:
            self.logger.error("error_setting_handlers")
            return False
        
        return True
    
    def openManager(self):
        """
        Opens the manager
        
        :rtype: boolean success status
        """
        if self.manager:
            try:
                self.manager.openManager()
                return True

            except Exception,e:
                self.logger.error("error_opening_phidget_manager")
                return False
        
        return False
            
    def testManager(self):
        """
        Performs a simple test to determine 
        if the manager appears OK
        """
        if not self.manager:
            return False
        
        try:
            attached_devices = self.manager.getAttachedDevices()
        except:
            return False
        
        return True


    def getDeviceInfo(self, device):
        """
        Retrieves information about a given ``device``
        """
        try:
            serial = device.getSerialNum()
            label  = device.getDeviceLabel()
            name   = device.getDeviceName()
            type   = device.getDeviceType()
            version= device.getDeviceVersion()
            
            return {'serial':serial,
                    'label':label,
                    'name':name,
                    'type':type,
                    'version':version 
                    }
        except:
                return None
        

    def _doLog(self, msg_id_success, msg_id_failure, device):
        ""
        info = self.getDeviceInfo(device)
        if info is not None:
            self.logger.info( msg_id_success, **info )
        else:
            self.logger.info( msg_id_failure )
            
        return info



    def logAttachEvent(self, phidget):
        """
        Logs an ``attach`` event for a device
        """
        try:    device=phidget.device
        except: 
            #dr = str(dir(phidget))
            #self.logger.error("logAttachEvent: dr[%s]" % dr)
            self.logger.error("error_phidget_device", event="attach")
            return
            
        info = self._doLog(    "info_phidget_attached", 
                        "info_phidget_attached_without_info", 
                        device
                        )
        
        return info
        
        
    def logDetachEvent(self, phidget):
        """
        Logs a ``detach`` event for a device        
        """
        try:    device=phidget.device
        except: 
            self.logger.error("error_phidget_device", event="detach")
            return
        
        info = self._doLog(    "info_phidget_detached", 
                        "info_phidget_detached_without_info", 
                        device
                        )

        return info


        
    # ======================================================================
    # ACTIONS from the Controller
    # ======================================================================

    
    def doAttach(self, phidget, *pargs):
        """
        """
        info = self.logAttachEvent(phidget)
        
        
    def doDetach(self, phidget, *pargs):
        """
        """
        info = self.logDetachEvent(phidget)
        

    def doError(self, error, *pargs):
        """
        """
        self.logger.error("error_phidget_error_event")


    def doAlarm(self, event, **kwargs):
        self.logger.info("in doAlarm")
        

    # ======================================================================
    # NOT USED
    # ======================================================================

    def _wireEvents(self, controller):
        """
        Wire the manager's event sources 
        to the target handlers
        
        :rtype: boolean success status
        """
        _wires = [  ('setOnAttachHandler',  'event_attach'),
                    ('setOnDetachHandler',  'event_detach'),
                    ('setOnErrorHandler',   'event_error'),
                  ]
        if self.manager:
            try:
                self._doWiring(self.manager, _wires, controller)
            except Exception,e:
                self.logger.error("error_setting_handlers")
                return False
            
            return True
        
        return False
    

    def _doWiring(self, source, table, target):
        """
        Wire 
        """
        for entry in table:
            set_method_name, event = entry
            source_set_method = getattr(source, set_method_name)
            self._buildAndWireProxy(source_set_method, event, target)


    def _buildAndWireProxy(self, source_set_method, event, target):
        """
        Builds a proxy between ``source`` and ``target``
        identified through ``event``
        """
        proxy = ProxyCallback(target, event)
        source_set_method(proxy)


