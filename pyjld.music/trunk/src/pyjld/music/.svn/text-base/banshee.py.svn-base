#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

import sqlite3

class BansheeDb():
    
    conn=None
    
    def __init__(self, file):
        self.conn = sqlite3.connect(file)

    def get(self, uri, fields="TrackId, Rating, PlayCount"):
        cursor=self.conn.cursor()
        cursor.execute("""select %s from CoreTracks where uri=:uri """ % fields, {"uri":uri})
        return cursor.fetchone()

        
    def update(self, uri, rating, playcount):
        cursor=self.conn.cursor()
        cursor.execute("""update CoreTracks set Rating=:rating, PlayCount=:playcount where uri=:uri""", 
                       {"uri":uri, "rating":rating, "playcount":playcount})
        self.conn.commit()
        return cursor.rowcount



class trackProc():
    """
    Uses an 'updater' object for updating
    the 'rating' & 'playcount' fields for a 'uri'
    """
    updater=None
    count=0
    
    def __init__(self, result_file=None, updater=None):
        self.updater=updater
        self.result_file = result_file
        
    def __call__(self, track):
        """
        Receive a track in the form of a dictionary
        """
        uri=track["location"]
        rating=track.get("rating",0)/20
        pc=track.get("play count", 0)
        #print "track: uri<%s>" % uri
        
        if (self.updater is not None):           
            result=self.updater.update(uri, rating, pc)
            if result != 1:
                print "! Track: uri<%s> rating<%s> playcount<%s>" % (uri, rating, pc)
            else:
                #print "Updated Track: uri<%s> rating<%s> playcount<%s>" % (uri, rating, pc)
                self.count+=1
                print "Update count<%s>" % self.count
                
            if self.result_file:
                if result != 1:
                    self.result_file.write("%s\n" % uri)
                    self.result_file.flush()


    
        

if __name__=="__main__":
    import os
    
    ifile="~/.config/banshee-1/banshee.db"
    file=os.path.expanduser(ifile)
    
    db=BansheeDb(file)
    uri="file:///mnt/music/__downloads2/TIGA%20-%20LIVE%20@%20STUDIO%2088.mp3"
    track=db.get(uri)
    
    print track
    
    rc=db.update(uri, 88, 77)
    print "rowcount: %s" % str(rc)

    
