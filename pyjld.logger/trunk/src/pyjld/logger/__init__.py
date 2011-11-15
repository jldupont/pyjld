#!/usr/bin/env python
"""
pyjld.logger: cross-platform logging utilities

This package consists mainly of:

    * MsgLogger: cross-platform logger with message translation
    * logger: a *ready-to-go* logger
    * xcLogger: a cross-platform syslog logger

=========
Changelog
=========

**0.7**

* Added ''auto-flush'' for all handlers that support it

**0.6**

* Added support for filters to MsgLogger class

**0.5**

* Added support for directly logging Exceptions with message_id & params

**0.4**

* Added daemon cooperation functionality: ``logger`` clears handlers associated with logger ``name`` 

**0.3* 

* More robust ``messages`` look-up in MsgLogger

**0.2*

* Added ``MsgLogger``

@author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__version__ = "0.7"
__fileid    = "$Id: __init__.py 53 2009-04-13 15:57:33Z jeanlou.dupont $"

__dependencies = []

__classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

from logger import *