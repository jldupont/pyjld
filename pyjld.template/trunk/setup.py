#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__fileid__  = "$Id: setup.py 7 2009-03-30 20:12:47Z jeanlou.dupont $"
__email     = "python (at) jldupont.com"

import sys
import textwrap
from setuptools import setup, find_packages

from pyjld.builder import findPackage


path, ns, package = findPackage()

this_module_name = "%s.%s" % (ns, package)
this_module = __import__( this_module_name )

print this_module_name

short_description, long_description = ( 
    textwrap.dedent(d).strip()
    for d in this_module.__doc__.split('\n\n', 1) )


__classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

__dependencies = []

setup(
    name             = this_module_name,
    description      = short_description,
    author_email     = __email,
    author           = __author__,
    url              = this_module.__doc_url,
    long_description = long_description,
    version          = this_module.__version__,
    package_data     = {'':['*.*']},
    packages         = find_packages('src'),
    classifiers      = __classifiers,
    install_requires = __dependencies,
    tests_require    = ['MiniMock >=1.0',],
    #test_suite       = ['tests.suite'],
    zip_safe         = True,
)

