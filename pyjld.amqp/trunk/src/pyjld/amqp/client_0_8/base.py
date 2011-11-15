#!/usr/bin/env python
"""
pyjld.amqp.client_0_8.base
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: base.py 64 2009-04-16 11:09:20Z jeanlou.dupont $"

__all__ = ['BaseException', 
           ]

from types import *



class BaseException(Exception):
    def __init__(self, message, msg_id, **kwargs):
        Exception.__init__(self, message)
        self.msg_id=msg_id
        self.params=kwargs


