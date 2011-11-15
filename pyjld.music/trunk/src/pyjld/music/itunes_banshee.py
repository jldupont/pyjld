#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
    
    Transfer Rating & PlayCount fields from
    iTunes Library to Banshee

"""
import os
import sys

from xml.sax import make_parser 
from xml.sax.handler import ContentHandler 

import itunes  as it
import banshee as ban
    
ifile="~/Music/iTunes Music Library.xml"
file=os.path.expanduser(ifile)

bifile="~/.config/banshee-1/banshee.db"
bfile=os.path.expanduser(bifile)

updater=ban.BansheeDb(bfile)

ripath="~/Music/itunes_banshee_result.txt"
rpath=os.path.expanduser(ripath)
rfile=open(rpath, "w")

btp=ban.trackProc(rfile, updater)

tp=it.trackProc(output=btp)
pp=it.nullPlaylistProc()

demux=it.itunesDemux(tp, pp)

lib=it.kvHandler(demux)

par=make_parser()
par.setContentHandler(lib)

datasource=open(file,"r")
par.parse(datasource)

rfile.close()
