#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: test.py 69 2009-04-17 18:49:17Z jeanlou.dupont $"

__all__ = ['',]

import logging
import sys

import pyjld.amqp.client_0_8.connection as amqp



formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ")
logger = logging.getLogger("pyjld.tsocket")
console = logging.StreamHandler(sys.stdout)
console.setFormatter(formatter)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)


conn=amqp.Connection("localhost",5672, logger=logger)

conn.write("AMQP\x01\x01\x09\x01")
conn.setup()

from twisted.internet import reactor
reactor.run()