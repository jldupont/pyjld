#!/usr/bin/env python

"""Copyright 2008 Phidgets Inc.
This work is licensed under the Creative Commons Attribution 2.5 Canada License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/2.5/ca/
"""

__author__ = 'Adam Stelmack'
__version__ = '2.1.5'
__date__ = 'October 23 2008'

#Basic imports
import time
from threading import *
from ctypes import *
import sys
#Phidget specific imports
from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Manager import *

dll = cdll.LoadLibrary("/usr/lib/libphidget21.so")
#LOGGER = CFUNCTYPE(c_int, c_char_p)
dll.CPhidget_enableLogging(6, "/var/log/phidget_test.log");

#Create an Manager object
manager = Manager()

#Event Handler Callback Functions
def inferfaceKitAttached(e):
    attached = e.device
    print "InterfaceKit %i Attached!" % (attached.getSerialNum())
    return 0

def interfaceKitDetached(e):
    detached = e.device
    print "InterfaceKit %i Detached!" % (detached.getSerialNum())
    return 0

#Main Program Code
try:
    manager.setOnAttachHandler(inferfaceKitAttached)
    #manager.setOnDetachHandler(interfaceKitDetached)
except PhidgetException, e:
    print "Phidget Exception %i: %s" % (e.code, e.message)
    print "Exiting...."
    exit(1)

print "Opening manager object...."

try:
    manager.openManager()
except PhidgetException, e:
    print "Phidget Exception %i: %s" % (e.code, e.message)
    print "Exiting...."
    exit(1)


time.sleep(10)

"""
print "Waiting for attach...."
try:
    manager.waitForAttach(10000)
except PhidgetException, e:
    print "1. Phidget Exception %i: %s" % (e.code, e.message)
    try:
        manager.closeManager()
    except PhidgetException, e:
        print "2. Phidget Exception %i: %s" % (e.code, e.message)
        print "Exiting...."
        exit(1)
    print "Exiting...."
    exit(1)
"""
print "Press Enter to quit...."

chr = sys.stdin.read(1)

print "Closing..."

try:
    manager.closeManager()
except PhidgetException, e:
    print "Phidget Exception %i: %s" % (e.code, e.message)
    print "Exiting...."
    exit(1)

print "Done."
exit(0)
