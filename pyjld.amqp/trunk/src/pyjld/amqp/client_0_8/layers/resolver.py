#!/usr/bin/env python
"""
pyjld.amqp.client_0_8.layers.resolver
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: resolver.py 68 2009-04-17 02:10:32Z jeanlou.dupont $"

__all__ = ['',]


_TABLE = {  #LAYER SOURCE    UP LAYER    DOWN LAYER    UP-SELECTOR
            "Protocol":     ("Frame",    None,         None),
            "Frame":        ("Method",   "Protocol",   "type"),
            "MethodFrame":  ("",         "Frame",      ),
            "HeaderFrame":  ("",         "Frame",      ),
            "BodyFrame":    ("",         "Frame",      ),
            "OOBMethod":    ("",         "Frame",      ),            
            "OOBHeader":    ("",         "Frame",      ),
            "OOBBody":      ("",         "Frame",      ),
            "Trace":        ("",         "Frame",      ),            
            "Heartbeat":    ("",         "Frame",      ),
          }

