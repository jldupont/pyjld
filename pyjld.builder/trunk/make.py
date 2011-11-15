#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: make.py 93 2009-10-09 20:12:44Z jeanlou.dupont $"

import os
import sys

from pyjld.os       import safe_mkdir, copyFiles, copyUpdatedFiles, safe_copytree
from pyjld.builder  import copyEggs, makeEggReleaseDir
from pyjld.builder  import findPackage, pprintFiles, keepBaseNames



# pkg_path/trunk/src
# pkg_path/trunk/dist
# pkg_path/tags/$version/eggs
# pkg_path/tags/$version/docs

## add the current path to the system path ##
## --
cwd=os.getcwd()
src=cwd+"/src"
sys.path.append(src)
#print sys.path


pkg_path, ns, package = findPackage()
this_module_name = "%s.%s" % (ns, package)
this_package     = __import__( this_module_name )
this_module      = getattr(this_package, package)
version          = this_module.__version__
tags_dir         = os.path.join(pkg_path, 'tags')

existed, release_path = makeEggReleaseDir( version, tags_dir )
if not existed:
    print "*** created eggs release directory [%s]" % release_path    


print "*** copying eggs to release directory"
#############################################
eggs_path = os.path.join( pkg_path, 'trunk', 'dist' )
files = copyUpdatedFiles(eggs_path, release_path)
files = keepBaseNames(files)
pprintFiles(files, "    copied [$src] to release directory" )


print "*** generating documentation"
####################################
docs_source = os.path.join( pkg_path, 'trunk', 'docs', 'source' )
docs_html   = os.path.join( pkg_path, 'trunk', 'docs', 'html' )
import sphinx
sphinx.main( ['sphinx', docs_source, docs_html] )


print "*** copying documentation to release directory"
######################################################
docs_html_release_path = os.path.join( pkg_path, 'tags', version)
safe_copytree(docs_html, docs_html_release_path, skip_dirs=['.svn',])

