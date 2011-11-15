"""
    Various classes for manipulating 
    iTunes Library.xml file

    @author: Jean-Lou Dupont
"""
from xml.sax.handler import ContentHandler 

class kvHandler(ContentHandler):
    """
    Extracts the (key, value) pairs and
    sends them to an 'output processor' (OP).
    
    The OP must be a callable object instance i.e.
    implement the __call__ method.
    """
    state="start_key"
    output=None    
    cKeyName=""
    cValueType=""
    cValue=""
    inChar=False

    possibleValueTypes=["string", "integer", "date"]
    
    def __init__(self, output):
        self.output=output
        
    def reset(self):
        self.cKeyName=""
        self.cValueType=""
        self.cValue=""
        
    def startElement(self, _name, _attrs):
        
        # just in case somebody at somepoint
        # slips/forgets a case...
        name=_name.lower()
        
        if (name=="plist"):
            return
        
        if (self.state=="start_key"):
            if (name=="array") or (name=="data"):
                return           
                
        if (self.state=="start_key"):
            if (name=="key"):
                self.reset()
                self.state="get_key_name"
        
        ## CASE:  <key>KeyName</key><array> ...
        if (self.state=="start_value"):
            if (name=="array") or (name=="dict"):
                self.state="start_key"
                self.output((self.cKeyName, name))
                
        if (self.state=="start_value"):
            if name in self.possibleValueTypes:
                self.cValueType=name
                self.state="get_value"
                
            # for <true/>  and  <false/> elements
            if (name=="true") or (name=="false"):
                self.output((self.cKeyName, name))
                self.state="start_key"

                
    def characters(self, ch):
        """
        Run an accumulator because we can't trust
        the SAX parser to return all the 'characters'
        of an element in one go
        """
        if ch is None or ch=="":
            return
            
        if self.state=="get_key_name":
            self.cKeyName+=ch
    
        if (self.state=="get_value"):
            self.cValue+=ch


    def endElement(self, name):
        if self.state=="get_key_name":
            self.cKeyName=self.cKeyName.lower()
            self.state="start_value"

        if (self.state=="get_value"):
            val=self.convert(self.cValueType, self.cValue)
            self.output((self.cKeyName, val))
            self.state="start_key"

        
    def convert(self, type, value):
        if type=="string" or type=="date":
            return str(value)
        
        if type=="integer":
            return int(value)
        
        return None




class itunesDemux(): 
    """
    Demultiplexes between the (key,value) pairs
    of the "Tracks" section of the Library file
    and the "Playlist" section.
    
    Sends the respective (key,value) pairs to the
    specified 'output processors'.
    """
    
    plDelim="playlists"  #lowercase...
    
    state=None
    trackProc=None
    playlistProc=None
    
    def __init__(self, trackProc, playlistProc):
        self.state="st_tracks"
        self.trackProc=trackProc
        self.playlistProc=playlistProc
    
    def __call__(self, elem):
        k,v = elem
        if (k==self.plDelim):
            self.state="st_playlist"
            self.trackProc(("end","end"))
            return
        sfunc=getattr(self, self.state)
        return sfunc(elem)
    
    def st_tracks(self, elem):
        self.trackProc(elem)
        
    def st_playlist(self, elem):
        self.playlistProc(elem)
        
        

        
class trackProc():
    """
    Track Processor
    """
    state=None
    musicfolder=None
    current={}
    output=None
    
    def __init__(self, output=None, keysToDrop=[]):
        self.state="st_start"
        self.musicfolder=None
        self.keysToDrop=keysToDrop
        self.output=output
    
    def __call__(self, elem):
        k,v=elem
        if (k=="end"):
            self.doTrackReady()
            
        sfunc=getattr(self, self.state)
        return sfunc(elem)

    def isInteger(self, var):
        try: 
            i=int(var)
            return True
        except:
            return False

    def st_start(self, elem):
        """
        Retrieves the Music Folder parameter
        """
        k,v=elem
        #print "st_start: (k,v): (%s, %s)" % (k,v)
        if (self.isInteger(k)):
            return
        if (k=="music folder"):
            self.musicfolder=v
            #print "Music Folder: " + v
        if (k=="tracks"): #lowercase....
            self.state="st_tracks"

    def st_tracks(self, elem):
        k,v=elem
        if (v=="dict"):
            return        
        #print "st_tracks: (k,v): (%s, %s)" % (k,v)
        if (self.isInteger(k)):
            return
     
        if (k=="track id"):
            self.doTrackReady()
            self.current={}

        self.maybeKeepKey(k,v)            
        
    def maybeKeepKey(self, key, value):
        """
        Filter out the fields we do not want
        """
        if key not in self.keysToDrop:
            self.current[key]=value
                
    def doTrackReady(self):
        if self.current=={}:
            return
        if (self.output is None):
            sorted=sortedDict(self.current )
            print "TRACK: " + str( sorted )
        else:
            self.output(self.current)


        
def sortedDict(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]




class playlistProc():
    """
    Playlist Processor
    """
    state=None
    current={}
    output=None
    
    def __init__(self, output=None):
        self.state="st_start"
        self.output=output

    def __call__(self, elem):
        k,v=elem
        if (k=="name"):
            self.doPlaylistReady()
            self.current={}
        
        self.current[k]=v
        
    def doPlaylistReady(self):
        if self.current=={}:
            return
        if (self.output is None):
            print "Playlist: " + str(sortedDict(self.current))
        else:
            self.output(self.current)
        


class nullPlaylistProc():
    def __call__(self, elem):
        pass


    
if __name__=="__main__":
    import os
    import sys
    from xml.sax import make_parser 
    from xml.sax.handler import ContentHandler 
    
    ifile="~/Music/iTunes Music Library (copy).xml"
    file=os.path.expanduser(ifile)


    tp=trackProc()
    pp=playlistProc()

    demux=itunesDemux(tp, pp)

    lib=kvHandler(demux)
    par=make_parser()
    par.setContentHandler(lib)

    
    datasource=open(file,"r")
    par.parse(datasource)

    
    
