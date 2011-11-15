#!/usr/bin/env python
"""
pyjld.amqp.client_0_8.logger

Logger helper functions
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: logger.py 61 2009-04-15 13:41:59Z jeanlou.dupont $"

__all__ = ['doLog',]


def doLog(logger, source, level, msg):
    if logger:
        message = "%s: %s" % (source, msg)
        method = getattr(logger, level)
        method( message )
