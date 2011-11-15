#!/usr/bin/env python
"""
pyjld.phidgets.bonjour.bus
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: bus.py 69 2009-04-17 18:49:17Z jeanlou.dupont $"

__all__ = ['busSignals',]

import dbus, dbus.service

    
class busSignals(dbus.service.Object):
    """
    Dbus signals
    """

    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SessionBus(), bus_name="pyjld.phidgets")

    @dbus.service.signal(dbus_interface='pyjld.phidget', signature='sss')
    def PhidgetFound(self, name, serial, type):
        pass
