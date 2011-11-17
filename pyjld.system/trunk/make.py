#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"

import os
import sys

cdir=os.getcwd()
while True:
    print cdir
    if cdir.endswith("/pyjld"):
        break
    cdir=os.path.dirname(cdir)

sys.path.insert(0, os.path.join(cdir, "pyjld.builder", "trunk", "src"))

from pyjld.builder.make  import make

make()
