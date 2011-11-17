#!/usr/bin/env python
""" 
pyjld.system: various system level utilities (e.g. daemon, cross-platform registry, command-line tools)

This package contains various system level utilities.

=========
Changelog
=========

*0.5*

* command.ui: ref_options are now optional
* added 'mswitch' & 'base' for agent design pattern

*0.4*

* Added ''proxy'' module
* Corrected "cmd_restart" from daemon module
* Added status return code to ui.handleError method 

*0.3*

* Modified BaseCmdUI.handleArgument: integrates the templating for usage message

*0.2*  

* Added command-line related utilities
* Added a cross-platform ``registry`` utility
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__version__ = "0.5"
__fileid    = "$Id: __init__.py 69 2009-04-17 18:49:17Z jeanlou.dupont $"


__classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

__dependencies = ['python_daemon',]

