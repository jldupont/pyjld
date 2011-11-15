#!/usr/bin/env python
"""
pyjld.os.tools

Various OS utilities

@author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: tools.py 96 2009-10-13 23:09:36Z jeanlou.dupont $"

__all__ = ['safe_mkdir','psyspaths','safe_oneup','safe_walkup', 'versa_copy',
           'copyFiles', 'copyUpdatedFiles', 'genUpdatedFiles',
           'safe_copytree', 'recursive_chmod'
           ]

import os
import shutil
import sys
from types import *


class pyjld_os_Error(EnvironmentError):
    pass



def safe_mkdir(path, mode=0777):
    """
    Safely creates a directory hierarchy
    
    This function does not throw an exception if the path already exists or
    is created successfully; this behavior contrasts with that of the 
    standard ``os.makedirs`` builtin i.e. throws an error if the path
    already exists.
    
    The function only fails if the child directory and its required parent
    hierarchy can not be created.
    
    The function accepts either a string or a list for the parameter ``path``.
    If ``path`` is a list, the function performs an ``os.path.join`` to construct
    the target path. 
    
    .. Parameters
    
    **Returns**: (existed, path)
    
    The function returns a boolean True if the directory already existed.
     
    """
    # expand list if necessary
    if type(path) is ListType:
        path = os.path.join(*path)

    
    try:    already_exists = os.path.isdir(path)
    except: already_exists = False
    
    if already_exists:
        return True, path
    
    try:    os.makedirs( path, mode )
    except: pass
    
    exists = os.path.exists(path)
    if not exists:
        raise RuntimeError("path[%path] can not be created. Is it a valid directory path?")

    # we obviously had to create it.
    return False, path


def versa_copy(src_file, target_path):
    """
    Copies the ``src_file`` to the ``target_path``
    
    The parameter ``src_file`` can be either a list consisting of
    `path fragments` or a just a string representing the filesystem path.
    
    **Returns**: ``(src_file, dest_file)``.
    
    """
    if type(src_file) is ListType:
        src_file = os.path.join(*src_file)

    base_name = os.path.basename( src_file )

    dest_file = os.path.join(target_path, base_name)
    shutil.copyfile(src_file, dest_file)

    return (src_file, dest_file)


def copyFiles(src_path, dest_path):
    """
    Copies all the files (non-recursive) from ``src_path``
    to ``dest_path``
    
    The function returns the tuple list of
    files copied i.e. ``(src_file, dest_file)``.
    
    **Returns**: list of files copied in the form ::

        [ (src_file, dest_file) ...]
    """
    files=[]
    src_files = os.listdir(src_path)
    for src_file_name in src_files:
        src_file  = os.path.join( src_path, src_file_name )
        dest_file = os.path.join( dest_path, src_file_name )
        shutil.copyfile( src_file, dest_file )
        files.append( (src_file, dest_file) )

    return files



def genUpdatedFiles(src_path, dest_path):
    """
    Generator which provides updated files by comparing
    the files in ``src_path`` to the files contained
    in ``dest_path``.
    
    **Returns**: each iteration provides a tuple of the form ::
    
        (src_file, dest_file)

    """
    src_files  = os.listdir(src_path)
    dest_files = os.listdir(dest_path)
    
    for src_file_name in src_files:
        src_file = os.path.join( src_path, src_file_name )
        src_stat = os.stat( src_file )
        src_mtime = src_stat.st_mtime
        
        dest_file = os.path.join( dest_path, src_file_name )
        try:
            dest_stat  = os.stat( dest_file )
            dest_mtime = dest_stat.st_mtime
        except:
            dest_mtime = 0L
            
        if src_mtime > dest_mtime:
            yield (src_file, dest_file)
            
    raise StopIteration



def copyUpdatedFiles(src_path, dest_path):
    """
    Copies only the updated files from ``src_path``
    to the destination directory ``dest_path``
    
    **Returns**: list of files copied in the form ::

        [ (src_file, dest_file) ...]
 
    """
    files=[]
    for src_file, dest_file in genUpdatedFiles(src_path, dest_path):
        shutil.copy(src_file, dest_file)
        files.append( (src_file, dest_file) )
    
    return files



def psyspaths():
    """
    Pretty print sys.path
    
    Usage ::
    
        >>> from pyjld.os import psyspaths
        >>> psyspaths()

    """
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint( sys.path )
    
    

def safe_oneup(path):
    """
    Goes up one level in the directory hierarchy starting from ``path``
    
    **Returns**: `None` when error/reached the top
    """
    try:    
        one_up = os.path.dirname( path )
        
        #Have we reached the top?
        if one_up == path:
            return None
    except: 
        return None
    return  one_up
    
    
    

def safe_walkup(path):
    """
    Safely walks up the directory hierarchy
    
    This function is implemented as a generator.

    Usage ::
    
        >>> cd = os.getcwd()
        >>> for path in safe_walkup(cd):
        ...     print path
    """
    path = safe_oneup(path)
    while(path is not None):
        yield path
        path = safe_oneup(path)
        
    raise StopIteration


## Quick and dirty because
## __builtins__ differs slightly between Python2.5 and Python2.6
try:
    WindowsError()
except:
    class WindowsError(Exception):
        pass
    


def safe_copytree(src, dst, symlinks=False, dir_mode=0777, skip_dirs=[], make_dirs=False):
    """
    Recursively copy a directory tree using copy2(). This function
    is meant to complement the less versatile ``shutil.copytree``.

    The destination directory may not already exist: missing directory
    paths are created on the fly with the ``dir_mode`` as mode.
    
    Directories can be skipped entirely using ``skip_dirs`` list ::
    
        ['.svn', '.doctree',]
    
    If exception(s) occur, an ``pyjld_os_Error`` is raised 
    with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied.
    """
    names = os.listdir(src)
    if make_dirs:
        os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                #JLD: skip dir?
                base_srcname = os.path.basename(srcname)
                if not base_srcname in skip_dirs:          
                    safe_copytree(srcname, dstname, 
                                  symlinks=symlinks, 
                                  dir_mode=dir_mode, 
                                  skip_dirs=skip_dirs,
                                  make_dirs=make_dirs)
            else:
                #JLD: make sure target directory exists
                safe_mkdir(dst, dir_mode)

                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except pyjld_os_Error, err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass     
    except OSError, why:
        errors.extend((src, dst, str(why)))
        
    if errors:
        raise pyjld_os_Error, errors


def recursive_chmod(path, 
                    mode=0775, 
                    do_files=True, 
                    do_dirs=True,
                    skip_files=[],
                    skip_dirs=[] ):
    """
    Recursive ``chmod``
    
    :param path: the top level starting path
    :param mode: the mode to apply
    :param do_files: to perform the operation on files
    :param do_dirs: to perform the operation on dirs
    :param skip_files: to skip files, list the basenames
    :param skip_dirs: to skip dirs, list the basenames
    """
    paths=[]
    for root, dirs, files in os.walk(path):
        if do_files:
            for filename in files:
                this_path = os.path.join(root, filename)
                base_name = os.path.basename( this_path )
                if base_name not in skip_files:
                    os.chmod(this_path, mode)
                    paths.append(this_path)
                
        if do_dirs:
            for _dir in dirs:
                this_path = os.path.join(root, _dir)
                base_name=os.path.basename(this_path)
                if base_name not in skip_dirs:
                    os.chmod(this_path, mode)
                    paths.append(this_path)
    return paths


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
