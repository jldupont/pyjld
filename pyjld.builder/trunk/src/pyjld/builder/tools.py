#!/usr/bin/env python
"""
pyjld.builder.tools

@author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: tools.py 24 2009-04-02 01:54:53Z jeanlou.dupont $"

__all__ = ['findPackage','extractNsPackage', 'findPackages', 'getShortAndLongDescription',
           'copyEggs', 'makeEggReleaseDir', 'pprintFiles', 'keepBaseNames',
           'makeModuleName',
           ]

import os
import textwrap
from string import Template
from pyjld.os import safe_walkup, safe_mkdir, versa_copy


def findPackages(root):
    """
    Retrieves the packages from the root path
    
    Verifies the :param root: directory for the presence of
    valid packages i.e. directory name of the form ::
    
        namespace.package
        
    """
    dir_list = os.listdir(root)
    
    packages=[]
    for path in dir_list:
        try:    
            ns, package = path.split('.')
            
            #filter out .svn etc.
            if ns:
                packages.append((path, ns, package))
        except: 
            continue

    return packages


def findPackage( root=os.getcwd() ):
    """
    Finds the package's root
    
    The package directory must be of the form ``ns.package``.
    The :param root: represents the starting directory in the
    child hierarchy of the said package.
    
    The default :param root: parameter is the current directory.
    
    """
    for path in safe_walkup(root):
        if path is None:
            return None, None, None
        
        name = os.path.basename( path )
        ns, package = extractNsPackage(name)      
        if ns is not None:
            return (path, ns, package)
        
    return None, None, None


def makeModuleName(ns, package):
    """
    """
    return "%s.%s" % (ns, package)


def extractNsPackage(name, filterEmptyNs=True):
    """
    Extracts the tuple (ns,package) from the specified name
    
    The parameter :param name: must correspond to a directory name.
    """
    ns, package = None, None
    
    try:    ns, package = name.split('.')
    except: pass

    if not ns:
        ns, package = None, None
        
    return ns, package


def getShortAndLongDescription(module):
    """
    Returns the short and long description documentation strings
    from a loaded module
    """
    try:
        short_description, long_description = ( 
        textwrap.dedent(d).strip()
        for d in module.__doc__.split('\n\n', 1) )
    except:
        raise RuntimeError('Error extracting short & long description from module [%s]' % str(module))
        
    return short_description, long_description


def makeEggReleaseDir(version, root):
    """
    Make an `egg` release directory in the `root` directory
    
    The directory path will be according to the following ::
    
        $root/$version/eggs

    """
    path = [root, version, 'eggs']
    existed, path = safe_mkdir(path)
    return existed, path


def copyEggs(list, source_pkg, release_dir):
    r"""
    Copies a list of eggs 
    
    :param list: eggs list
    :param source_pkg: the source directory
    :param release_dir: the target directory    
    
    The egg list is of the form ::
    
        [ (egg_type, egg_version, egg_name), ... ]
    
    The function returns the list of files copied in the form ::
        
        [ (src_file, dest_file), ... ]

    """
    files=[]
    for egg_type, egg_version, egg_name in list:
        src_file, dest_file = versa_copy([source_pkg, 'trunk', egg_name], release_dir)
        files.append((src_file, dest_file))
        
    return files



def pprintFiles( files, base_msg ):
    """
    Pretty prints a list of file names using :param base_msg: 
    message as string template
    
    The template parameters declared are:
    
    * `src`
    * `dest`
    
    """
    tpl = Template(base_msg)
    for file in files:
        src_file, dest_file = file
        print tpl.safe_substitute(src=src_file, dest=dest_file)


def keepBaseNames(files):
    """
    Maps the :param files: list consisting of ::
        
        [ (src_file, dest_file) ]
        
    to their basenames.
    """
    newList = []
    for file in files:
        src_file, dest_file = file
        base_src  = os.path.basename(src_file)
        base_dest = os.path.basename(dest_file)
        newList.append((base_src, base_dest))
    return newList