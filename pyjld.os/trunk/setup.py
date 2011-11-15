#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__fileid__  = "$Id: setup.py 77 2009-05-04 18:10:24Z jeanlou.dupont $"
__email     = "python (at) jldupont.com"

import os
import sys
from setuptools import setup, find_packages

from pyjld.builder import findPackage, getShortAndLongDescription

#helps with Eclipse external buidler

#__file__dir = os.path.dirname( __file__ )
#os.chdir(__file__dir)

__file__dir = os.getcwd()
print __file__dir

pkg_path, ns, package = findPackage(__file__dir)
this_module_name = "%s.%s" % (ns, package)
this_package     = __import__( this_module_name )
this_module      = getattr(this_package, package)
version          = this_module.__version__

short_description, long_description = getShortAndLongDescription(this_module) 

_doc_url = "http://pyjld.googlecode.com/svn/trunk/%s.%s/tags/%s/docs/index.html" % (ns,package,version)

dist = setup(
    name             = this_module_name,
    description      = short_description,
    author_email     = __email,
    author           = __author__,
    url              = _doc_url,
    long_description = long_description,
    version          = this_module.__version__,
    package_data     = {'':['*.*']},
    namespace_packages=[ns],
    package_dir      = {'':'src'},
    packages         = find_packages('src'),
    classifiers      = this_module.__classifiers,
    install_requires = this_module.__dependencies,
    tests_require    = [],
    #test_suite       = ['tests.suite'],
    zip_safe         = True,
)

