#!/usr/bin/env python
"""
pyjld.phidgets.bonjour.controller

** NOT USED **

"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: controller.py 69 2009-04-17 18:49:17Z jeanlou.dupont $"

__all__ = ['controller_factory',]

import signal

from pyfse import Controller, pyfseException

from pyjld.system.proxy import ProxyCallback

transitions_table = {
            
            #current, event                #next, action
            #==============                =============
            
            #kickstart           
            ('', None):                     ('state_init',      None),
            
            # INIT state
            ('state_init', 'event_attach'): ('state_wait',      'doAttach'),
            ('state_init', 'event_detach'): ('state_wait',      'doDetach'),
            ('state_init', 'event_error'):  ('state_init',      'doError'),       #not supposed to occur with Phidget21 library
            ('state_init', 'event_alarm'):  ('state_init',      None),            
            
            # WAIT state (main loop)
            ('state_wait', 'event_attach'): ('state_wait',      'doAttach'),
            ('state_wait', 'event_detach'): ('state_wait',      'doDetach'),
            ('state_wait', 'event_error'):  ('state_wait',      'doError'),
            ('state_wait', 'event_alarm'):  ('state_wait',      'doAlarm'),
            
         }

# =========================================================================
# =========================================================================



def controller_factory( actions, logger ):
    """
    Builds a controller
    """
    return PhidgetsBonjourController( transitions_table, actions=actions, logger=logger )



# =========================================================================
# =========================================================================



class PhidgetsBonjourController(Controller):
    """
    The finite state-machine controller
    """
    _retry_timeout = 15 #seconds
    _reset_timeout = 15 #15*60 # 15minutes

    def __init__(self, table, actions=None, logger=None):
        Controller.__init__(self, table, actions=actions)
        self.logger = logger        
        

    def enter_state_init(self, event, *pargs, **kwargs):
        """
        Initialize / resets the state-machine
        """
        self.logger.info("state_init: begin")
                
        result = self.actions.createManager()
        if not result:
            self.logger.error("error_creating_phidgets_manager")
            return
        
        result = self.actions.wireEvents(self)
        if not result:
            self.logger.error("error_setting_handlers")
            return
        
        #if we fail here, we'll get an alarm anyways
        result = self.actions.openManager()
        if not result:
            self.logger.error("error_opening_phidget_manager")
            return

        self.logger.info("state_init: end")

    def enter_state_wait(self, event, *pargs, **kwargs):
        """
        Main state - wait for an attach/detach event
        """
        return

        self.logger.info("state_wait: begin - event[%s]" % event)
        if pargs:
            self.logger.info("state_wait: begin - pargs[%s]" % pargs)
            
        #self._scheduleAlarm(self._reset_timeout)
        self.logger.info("state_wait: end")

        
    # ==================================================
    #
    # ==================================================
    
    def _cancelSchedule(self):
        signal.alarm(0)
    
    def _scheduleAlarm(self, timeout=None):
        """
        Prepares a system alarm
        """
        if timeout is None:
            timeout = self._retry_timeout
        signal.alarm( timeout )

        

