#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
import httplib


def doHead(site, url):
    conn=httplib.HTTPConnection(site)
    conn.request("HEAD", url)
    resp=conn.getresponse()
    return resp

def doGet(site, url):
    """
    Performs an HTTP GET request
    """
    conn=httplib.HTTPConnection(site)
    conn.request("GET", url)
    resp=conn.getresponse()
    return resp


def getEtag(site, url):
    """
    Retrieves the ETag header of a URI
    through an HTTP HEAD method
    """
    conn=httplib.HTTPConnection(site)
    conn.request("HEAD", url)
    resp=conn.getresponse()
    return resp.getheader("etag")


def safeGet(site, url):
    """
    Performs an HTTP GET whilst trapping exceptions
    
    @return ("ok", Data) | (error, Error)
    """
    try:
        resp=doGet(site,url)
        ret=("ok", resp)
    except Exception,e:
        ret=("error", e)
    finally:
        return ret
    



if __name__=="__main__":

    site="stackoverflow.com"
    url="/feeds/user/171461"
    
    resp=safeGet(site, url)
    code, data=resp
    if (code=="resp"):
        print data.getheaders()
    else:
        print "Error: %s" % str(e)
        
    

