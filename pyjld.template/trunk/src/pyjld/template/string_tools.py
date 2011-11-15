#!/usr/bin/env python
"""
pyjld.template.string_tools

@author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: string_tools.py 36 2009-04-03 01:57:34Z jeanlou.dupont $"

__all__ = ['ExTemplate','safe_subvars',]


import string


class ExTemplate(string.Template):
    """
    String Template to ease integration with other string processing modules e.g. OptionParser
    """
    
    # must appear here to shadow the base class
    delimiter = '^^'
    
    def __init__(self, init):
        string.Template.__init__(self, init)




def safe_subvars(msg, **params):
    """
    Substitutes the keyword parameters in the string template
    """
    tpl = string.Template(msg)
    return tpl.safe_substitute( params )
