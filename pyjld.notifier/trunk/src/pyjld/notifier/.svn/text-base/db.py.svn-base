"""
    @author: Jean-Lou Dupont
"""

import os
import sys
import sqlite3
from pyjld.os import safe_mkdir


class NotifierDb(object):
    """
    SQLITE database for holding the journal of
    url visited by the Notifier engine
    """
    dbfile="~/.pyjld/notifier.db"
    path=""
    conn=None
    keys=["site", "url", "feed", "version", "last_updated", "data", "code"]
    
    def __init__(self):
        self.path=os.path.expanduser(self.dbfile)
        
    def create_dir(self):
        """
        Creates the directory hierarchy leading to
        the database file IFF it does not exist 
        already
        """
        try:
            dir=os.path.dirname(self.path)
            safe_mkdir(dir)
        except:
            return ("error", "cannot create directory hierarchy")
        
        return None
        
        
    def init(self):
        """
        Initialize the connection and the table(s)
        """
        r=self.create_dir()
        if (r is not None):
            return r
        
        try:
            self.conn=sqlite3.connect(self.path)
        except:
            return ("error", "cannot open db")
        
        c=self.conn.cursor()
        c.execute("""create table if not exists urls (
                site text,
                url text, 
                feed text,
                version text,
                last_updated text,
                code text,
                data text
                )""")
        
        self.conn.commit()
        return None


    def getlist(self):
        """
        Returns the all the entries in the form
        of a list of dict
        """
        if (self.conn is None):
            return ("error", "not initialized")
        
        c=self.conn.cursor()
        c.execute("""
            select * from urls
        """)
        
        return c.fetchall()

    def get(self, site, url):
        """
        Retrieve a specific element
        """
        sql="""
            select * from urls where site=? AND url=?
        """
        c=self.conn.cursor()
        c.execute(sql, [site, url])
        return c.fetchall()


    def getlistk(self):
        """
        Retrieves the list of entries in dict format
        """
        keys=""
        for key in self.keys:
            if keys != "":
                keys+=", "
            keys+="%s" % key
            
        sql="""select %s from urls
        """ % keys
        print sql
        c=self.conn.cursor()
        c.execute(sql)
        entries=c.fetchall()
        
        result=[]
        for entry in entries:
            dic={}
            pos=0
            for key in self.keys:
                value=entry[pos]
                dic[key]=value
                pos+=1
            result.append(dic)
        
        return result
                
        

    def update(self, site, url, **kwargs):
        """
        Only update the keys != None
        """
        keys=[]   ;  values=[]   ;   sets=""
        for k in kwargs:
            if k not in self.keys:
                raise Exception("invalid key: %s" % k)
            if sets is not "":
                sets += ", "
            sets+="%s=? " % k
            keys.append(k)
            values.append(kwargs[k])
        
        sql= """ update urls set %s where site=? AND url=?
        """ % sets
        
        params=values + [site, url]
        
        c=self.conn.cursor()
        c.execute(sql, params)
        self.conn.commit()
        
        return c.rowcount




        
if __name__=="__main__":
    
    n=NotifierDb()
    print n.init()
    print n.getlist()
    
    print n.update(site="test",url="test", version="123", code="200")
    
    print n.get("")
    
        