#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: make.py 14 2009-03-31 19:23:03Z jeanlou.dupont $"

import os
import sys

from pyjld.os       import safe_mkdir, copyFiles, copyUpdatedFiles, safe_copytree
from pyjld.builder  import copyEggs, makeEggReleaseDir
from pyjld.builder  import findPackage, pprintFiles, keepBaseNames

# pkg_path/trunk/src
# pkg_path/trunk/dist
# pkg_path/tags/$version/eggs
# pkg_path/tags/$version/docs


def target_eggsdir(version, tags_dir):
    existed, release_path = makeEggReleaseDir( version, tags_dir )
    if not existed:
        print "*** created eggs release directory [%s]" % release_path  
        
    return release_path  


def target_eggscopy(pkg_path, release_path):
    print "*** copying eggs to release directory"
    #############################################
    eggs_path = os.path.join( pkg_path, 'trunk', 'dist' )
    files = copyUpdatedFiles(eggs_path, release_path)
    files = keepBaseNames(files)
    pprintFiles(files, "    copied [$src] to release directory" )


def target_gendocs(docs_source, docs_html):
    print "*** generating documentation"
    ####################################
    import sphinx
    sphinx.main( ['sphinx', docs_source, docs_html] )


def target_copydocs(pkg_path, version, docs_html):
    print "*** copying documentation to release directory"
    ######################################################
    docs_html_release_path = os.path.join( pkg_path, 'tags', version, 'docs')
    safe_copytree(docs_html, docs_html_release_path, skip_dirs=['.svn',])


def make():
    pkg_path, ns, package = findPackage()
    this_module_name = "%s.%s" % (ns, package)
    this_package     = __import__( this_module_name )
    this_module      = getattr(this_package, package)
    version          = this_module.__version__
    tags_dir         = os.path.join(pkg_path, 'tags')
    
    docs_source = os.path.join( pkg_path, 'trunk', 'docs', 'source' )
    docs_html   = os.path.join( pkg_path, 'trunk', 'docs', 'html' )
    
    #targets
    release_path = target_eggsdir(version, tags_dir)
    target_eggscopy(pkg_path, release_path)
    target_gendocs(docs_source, docs_html)
    target_copydocs(pkg_path, version, docs_html)

# ==============================================
# ==============================================

if __name__ == "__main__":
    sys.exit( make() )