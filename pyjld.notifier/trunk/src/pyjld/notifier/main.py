"""
    @author: Jean-Lou Dupont
    
    For each URI:
        - HEAD request
        - IF ETag and/or Last-Modified
            - CHECK freshness
            - DOWNLOAD data if necessary
            - UPDATE db accordingly
          ELSE
            - GET request
            - IF feed
                - PARSE it
                - check "updated" field
                - UPDATE db
                
"""

import os, sys

from pyjld.notifier import db, tools


def listiter(list):
    for entry in list:
        yield entry

class Notifier():
    
    def __call__(self, notif):
        print "Notifier: %s\n" % notfi
    
    


class FeedProcessor():
    
    notifier=None
    
    def __init__(self, notifier):
        self.notifier=notifier
        
    def __call__(self, entry):
        site=entry['site']
        url =entry['url']
        head_response=tools.doHead(site, url)
        
    
    
            

class EntryProcessor():

    notifier=None

    def __init__(self, notifier):
        self.notifier=notifier


    def __call__(self, entry):
        ""
        
        

class Processor():
    
    def __init__(self, feedproc, pageproc=None):
        self.feedproc=feedproc
        self.pageproc=pageproc
        
    def process(self, entries):
        for entry in entries:
            if entry['feed']:
                self.dofeedentry(entry)
            else:
                self.dopageentry(entry)
                
    def dofeedentry(self, entry):
        if self.feedproc is not None:
            self.feedproc(entry)
            
    def dopageproc(self, entry):
        if self.pageproc is not None:
            self.pageproc(entry)
            

    
    

    

def main():
    ndb=db.NotifierDb()
    ndb.init()
    
    entries=ndb.getlistk()
    print entries

    n=Notifier()
    fp=FeedProcessor(n)
    p=Processor(fp)
    
    
    
main()
