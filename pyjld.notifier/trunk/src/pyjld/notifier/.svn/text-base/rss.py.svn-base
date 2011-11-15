#!/usr/bin/env python
"""
    RSS feed parser using SAX
    
    @author: Jean-Lou Dupont
"""
from xml.sax.handler import ContentHandler

class rssHandler(ContentHandler):
    """
    """
    state="header"
    capture=False
    header={}
    cKey=None
    cAttrs={}
    cCapture=""
    cEntry={}
    
    def __init__(self, output=None):
        self.output=output
        
    def emit(self, elem):
        if (self.output is not None):
            self.output(elem)
            
    def extractAttrs(self, attrs):
        result={}
        for a in attrs.getNames():
            result[a]=attrs.getValue(a)
        return result
        
    # ===================================================================
    # SAX callback methods
    # ===================================================================
                
    def startElement(self, _name, _attrs):      
        # just in case somebody at somepoint
        # slips/forgets a case...
        name=_name.lower()
        getattr(self, "st_start_%s" % self.state)(name, _attrs)
                 
    def characters(self, ch):
        if (self.capture):
            self.cCapture+=ch

    def endElement(self, name):
        getattr(self, "st_end_%s" % self.state)(name)
    
    # ===================================================================
    # STATE: HEADER
    # ===================================================================
        
    def st_start_header(self, name, _attrs):
        if (name=="entry"):
            self.state="entry"
            self.capture=True
            self.emit(("header", self.header))
        else:
            self.cKey=name
            self.capture=True
        
    def st_end_header(self,name):
        if (self.capture):
            self.header[self.cKey]=self.cCapture
            self.cCapture=""
            self.capture=False

    # ===================================================================
    # STATE: ENTRY
    # ===================================================================
    def st_start_entry(self, name, attrs):
        #print "start <%s>" % name
        if (self.cEntry=="entry"):
            self.cEntry={}
            self.cKey=None
        else:
            self.cKey=name
            self.cAttrs=attrs
            self.cCapture=""
    
    def st_end_entry(self, name):
        #print "end <%s>" % name
        if (name=="entry"):
            self.emit(("entry", self.cEntry))
            self.cEntry={}
            self.cKey=None
            self.cCapture=""
        else:
            if (self.cKey is not None):
                attrs=self.extractAttrs(self.cAttrs)
                #print "  <(%s, %s, %s)>" % (self.cKey, attrs, self.cCapture)
                self.cEntry[self.cKey]=(attrs, self.cCapture)
                self.cCapture=""

    
    

class simpleReceptor():
    """
    For testing purposes 
    """
    def __call__(self, elem):
        type, data=elem
        print "Type: %s  Data<%s>" % (type, data)




def extractUpdated(feed):
    """
    Extracts the <updated> element text
    from an RSS feed 
    """
    
    
if __name__=="__main__":
    
    testFeed="""
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:creativeCommons="http://backend.userland.com/creativeCommonsRssModule" xmlns:thr="http://purl.org/syndication/thread/1.0"> 
    <title type="text">User Jean-Lou Dupont - Stack Overflow</title> 
    <link rel="self" href="http://stackoverflow.com/feeds/user/171461" type="application/atom+xml" /> 
    <link rel="alternate" href="http://stackoverflow.com/users/171461" type="text/html" /> 
    <subtitle>most recent 30 from stackoverflow.com</subtitle> 
    <updated>2009-10-06T01:03:38Z</updated> 
    <id>http://stackoverflow.com/feeds/user/171461</id> 
    <creativeCommons:license>http://www.creativecommons.org/licenses/by-nc/2.5/rdf</creativeCommons:license> 
 
    <entry> 
        <id>http://stackoverflow.com/questions/1522867/python-how-do-you-setup-your-workspace-on-ubuntu</id> 
        <title type="text">python: how do you setup your workspace on Ubuntu?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="python"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="eclipse"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1522867/python-how-do-you-setup-your-workspace-on-ubuntu" /> 
        <published>2009-10-05T23:10:22Z</published> 
        <updated>2009-10-05T23:16:54Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Lets say I have my workspace (on Eclipse) where I develop my Python modules and I would like to &quot;link&quot; my working files to system Python paths.  I know I can drop .pth files etc. but I would like to get the community's wisdom as to the best practices.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1517984/banshee-how-would-i-set-the-rating-for-a-specific-track-on-banshee-through-dbus</id> 
        <title type="text">banshee: How would I set the rating for a specific track on Banshee through DBus?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="dbus"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="banshee"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="python"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1517984/banshee-how-would-i-set-the-rating-for-a-specific-track-on-banshee-through-dbus" /> 
        <published>2009-10-05T02:11:39Z</published> 
        <updated>2009-10-05T02:11:39Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I'd like to set the 'rating' of a specific track (i.e. not only the one currently playing) on Banshee through the DBus interface?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1515469/debian-does-apt-get-support-302-redirects</id> 
        <title type="text">debian: does apt-get support 302 redirects?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="apt-get"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="debian"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1515469/debian-does-apt-get-support-302-redirects" /> 
        <published>2009-10-04T02:46:54Z</published> 
        <updated>2009-10-04T04:14:11Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Will &lt;em&gt;apt-get&lt;/em&gt; follow 302 redirects if instructed?&lt;/p&gt;
 
&lt;p&gt;&lt;strong&gt;Clarifications&lt;/strong&gt;&lt;/p&gt;
 
&lt;p&gt;I have my own DEBIAN repositories and I am in the process of evaluating if I can &quot;virtually consolidate&quot; all of them to one.  For this, I need to understand if client side apt-get can follow 302 redirects since the &quot;virtual repo&quot; would use this &quot;trick&quot; to have apt-get fetch .deb package from different places.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver</id> 
        <title type="text">Python Pypi: what is your process for releasing packages for different Python versions? (Linux)</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="python"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="pypi"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="release-management"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver" /> 
        <published>2009-10-03T02:45:36Z</published> 
        <updated>2009-10-03T15:22:02Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I've got several eggs I maintain on Pypi but up until now I've always focused on Python 2.5x.
I'd like to release my eggs under both Python 2.5 &amp;amp; Python 2.6 in an automated fashion i.e.&lt;/p&gt;
 
&lt;ol&gt;
&lt;li&gt;running tests &lt;/li&gt;
&lt;li&gt;generating doc&lt;/li&gt;
&lt;li&gt;preparing eggs&lt;/li&gt;
&lt;li&gt;uploading to Pypi&lt;/li&gt;
&lt;/ol&gt;
 
&lt;p&gt;How do you guys achieve this?&lt;/p&gt;
 
&lt;p&gt;A related question: how do I tag an egg to be &quot;version independent&quot; ? works under all version of Python?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1513664/debian-repo-is-there-a-way-to-include-a-complete-uri-for-the-download-path-in-th</id> 
        <title type="text">debian repo: Is there a way to include a complete URI for the download path in the Packages.gz file?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="debian"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="repository"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1513664/debian-repo-is-there-a-way-to-include-a-complete-uri-for-the-download-path-in-th" /> 
        <published>2009-10-03T12:52:59Z</published> 
        <updated>2009-10-03T14:53:20Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I have several DEBIAN repositories I would like to &quot;virtually&quot; consolidate i.e. have one location for the Packages.gz file whilst having the &quot;download links&quot; for each package listed be located somewhere else (not the same server).&lt;/p&gt;
 
&lt;p&gt;Is this possible?&lt;/p&gt;
 
&lt;p&gt;&lt;strong&gt;Example:&lt;/strong&gt;&lt;/p&gt;
 
&lt;ul&gt;
&lt;li&gt;&lt;p&gt;Repositories X, Y, Z&lt;/p&gt;&lt;/li&gt;
&lt;li&gt;&lt;p&gt;Virtual Repository V with Packages.gz entries&lt;/p&gt;
 
&lt;ul&gt;
&lt;li&gt;&lt;p&gt;X1, X2 etc.&lt;/p&gt;&lt;/li&gt;
&lt;li&gt;&lt;p&gt;Y1, Y2 etc.&lt;/p&gt;&lt;/li&gt;
&lt;/ul&gt;&lt;/li&gt;
&lt;/ul&gt;
 
&lt;p&gt;&lt;strong&gt;Implementation Suggestion&lt;/strong&gt;&lt;/p&gt;
 
&lt;p&gt;Assuming apt-get support it, I intend to write a Google AppEngine application that would fetch on a regular basis the Packages.gz files from the source repositories and &lt;em&gt;consolidate&lt;/em&gt; them in one repository &lt;em&gt;V&lt;/em&gt;.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator</id> 
        <title type="text">python: is there an XML parser implemented as a generator?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="python"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="generator"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="xml"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="parsing"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator" /> 
        <published>2009-10-03T12:14:31Z</published> 
        <updated>2009-10-03T14:01:20Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I'd like to parse a big XML file &quot;on the fly&quot;. I'd like to use a python generator to perform this.  I've tried &quot;iterparse&quot; of &quot;xml.etree.cElementTree&quot; (which is really nice) but still not a generator.&lt;/p&gt;
 
&lt;p&gt;Other suggestions?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
<entry> 
    <id>http://stackoverflow.com/questions/1382569/debian-packaging-of-a-python-package/1513677#1513677</id> 
    <title type="text">Answer by Jean-Lou Dupont for Debian packaging of a Python package.</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1382569/debian-packaging-of-a-python-package/1513677#1513677" /> 
    <published>2009-10-03T12:57:20Z</published>   
    <updated>2009-10-03T12:57:20Z</updated> 
    <summary type="html">&lt;p&gt;I've crafted a couple of different ways using Python. One example (which you would most probably need to adapt to fit your needs ;-) is available &lt;a href=&quot;http://code.google.com/p/erlang-mswitch/source/browse/trunk/make.py&quot; rel=&quot;nofollow&quot;&gt;here&lt;/a&gt;.&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1509213/embed-indentifier-within-an-email/1509235#1509235</id> 
    <title type="text">Answer by Jean-Lou Dupont for Embed indentifier within an Email</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1509213/embed-indentifier-within-an-email/1509235#1509235" /> 
    <published>2009-10-02T12:30:33Z</published>   
    <updated>2009-10-02T12:30:33Z</updated> 
    <summary type="html">&lt;p&gt;While I can't say for certain, my investigation in that sort of matter some time ago yielded the following &quot;conclusion&quot;:&lt;/p&gt;
 
&lt;ol&gt;
&lt;li&gt;Headers are transformed a lot&lt;/li&gt;
&lt;li&gt;Message bodies are transformed a lot&lt;/li&gt;
&lt;/ol&gt;
 
&lt;p&gt;This is partly because, I suspect, of:&lt;/p&gt;
 
&lt;ol&gt;
&lt;li&gt;Need to protect users from malicious intentions&lt;/li&gt;
&lt;li&gt;Need to perform &quot;targeted marketing&quot; &lt;/li&gt;
&lt;/ol&gt;
 
&lt;p&gt;I have seen &quot;unique codes&quot; flying around in clear text in the email body but I would suggest having a unique identifier embedded in the return address instead.&lt;/p&gt;
</summary> 
</entry> 
    <entry> 
        <id>http://stackoverflow.com/questions/1507477/dbus-problem-with-dbusbusgetuniquename</id> 
        <title type="text">dbus: problem with dbus_bus_get_unique_name</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="dbus"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1507477/dbus-problem-with-dbusbusgetuniquename" /> 
        <published>2009-10-02T02:18:35Z</published> 
        <updated>2009-10-02T12:25:38Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I am having an issue with DBus:&lt;/p&gt;
 
&lt;ol&gt;
&lt;li&gt;I register with DBus *dbus_bus_get()* method : OK&lt;/li&gt;
&lt;li&gt;I add filter matches : OK&lt;/li&gt;
&lt;li&gt;I add a filter callback function: OK&lt;/li&gt;
&lt;li&gt;I start a dispatch loop through *dbus_connection_read_write_dispatch()* : OK&lt;/li&gt;
&lt;/ol&gt;
 
&lt;p&gt;Everything works OK.  Now, if I insert:&lt;/p&gt;
 
&lt;p&gt;1a. *dbus_bus_get_unique_name()*&lt;/p&gt;
 
&lt;p&gt;I get a nasty exception message:&lt;/p&gt;
 
&lt;blockquote&gt;
  &lt;p&gt;arguments to *dbus_connection_send_with_reply_and_block()* were incorrect, assertion &quot;(error) == NULL || !*dbus_error_is_set ((error))*&quot; failed in file dbus-connection.c line 3301.&lt;/p&gt;
&lt;/blockquote&gt;
 
&lt;p&gt;Help please.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
<entry> 
    <id>http://stackoverflow.com/questions/1507477/dbus-problem-with-dbusbusgetuniquename/1509215#1509215</id> 
    <title type="text">Answer by Jean-Lou Dupont for dbus: problem with dbus_bus_get_unique_name</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1507477/dbus-problem-with-dbusbusgetuniquename/1509215#1509215" /> 
    <published>2009-10-02T12:25:38Z</published>   
    <updated>2009-10-02T12:25:38Z</updated> 
    <summary type="html">&lt;p&gt;After some experimentation, it seems that the function &lt;strong&gt;dbus_bus_get_unique_name()&lt;/strong&gt; must be called from within a specific context.  I managed to get a meaningful result when accessing this function through a &lt;strong&gt;filter callback&lt;/strong&gt; function e.g. one registered with &lt;strong&gt;dbus_add_filter&lt;/strong&gt; function.&lt;/p&gt;
</summary> 
</entry> 
    <entry> 
        <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file</id> 
        <title type="text">make: hierarchical make file</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="build-process"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="makefile"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="make"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file" /> 
        <published>2009-09-30T13:43:54Z</published> 
        <updated>2009-09-30T14:56:42Z</updated> 
        <summary type="html"> 
            &lt;p&gt;(disclaimer: I am used to scons ... I am somewhat unexperienced with make)&lt;/p&gt;
 
&lt;p&gt;Context: I am using Eclipse CDT which generates makefiles.&lt;/p&gt;
 
&lt;p&gt;Let's say I have a project directory 'lib' and 2 build configurations 'Debug' and 'Release'. Eclipse CDT gracefully generates a makefile for each build configuration.  The said makefiles end-up residing in 'Debug' and 'Release' folders.&lt;/p&gt;
 
&lt;p&gt;Now, what I want to do is have a makefile in the folder 'lib' which &lt;em&gt;calls&lt;/em&gt; the makefiles 'Debug/makefile' and 'Release/makefile'.&lt;/p&gt;
 
&lt;p&gt;How do I do that?&lt;/p&gt;
 
&lt;p&gt;I want to be able to launch 'make' in the folder 'lib' and both configurations would be called with the specified target(s).&lt;/p&gt;
 
&lt;p&gt;&lt;strong&gt;Solution&lt;/strong&gt;
Based on all the great input gathered here, I devised the following:&lt;/p&gt;
 
&lt;pre&gt;&lt;code&gt;MAKE=make
BUILDS=Release Debug
TARGETS=all clean
 
$(TARGETS):
    @for b in $(BUILDS) ; do $(MAKE) -C $$b $@ ; done
 
$(BUILDS):
    @for t in $(TARGETS) ; do $(MAKE) -C $@ $$t ; done
 
%:
    @for b in $(BUILDS) ; do $(MAKE) -C $$b $@ ; done
&lt;/code&gt;&lt;/pre&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1488514/erlang-eigettype-where-are-the-defined-constants-for-the-type-field</id> 
        <title type="text">erlang: ei_get_type() : where are the defined constants for the 'type' field?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="erlang"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="erl-interface"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="ei"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1488514/erlang-eigettype-where-are-the-defined-constants-for-the-type-field" /> 
        <published>2009-09-28T18:10:30Z</published> 
        <updated>2009-09-29T19:34:49Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I am trying to use *ei_get_type()* (&lt;a href=&quot;http://www.erlang.org/doc/man/ei.html&quot; rel=&quot;nofollow&quot;&gt;ei&lt;/a&gt;) but I am having trouble finding where the 'type' field is documented. I've looked in &lt;strong&gt;ei.h&lt;/strong&gt; but all I could find was a list of constants starting with &quot;ERL_&quot;.&lt;/p&gt;
 
&lt;pre&gt;&lt;code&gt;#define ERL_SMALL_INTEGER_EXT 'a'
#define ERL_INTEGER_EXT       'b'
#define ERL_FLOAT_EXT         'c'
#define ERL_ATOM_EXT          'd'
#define ERL_REFERENCE_EXT     'e'
#define ERL_NEW_REFERENCE_EXT 'r'
#define ERL_PORT_EXT          'f'
#define ERL_PID_EXT           'g'
#define ERL_SMALL_TUPLE_EXT   'h'
#define ERL_LARGE_TUPLE_EXT   'i'
#define ERL_NIL_EXT           'j'
#define ERL_STRING_EXT        'k'
#define ERL_LIST_EXT          'l'
#define ERL_BINARY_EXT        'm'
#define ERL_SMALL_BIG_EXT     'n'
#define ERL_LARGE_BIG_EXT     'o'
#define ERL_NEW_FUN_EXT   'p'
#define ERL_FUN_EXT           'u'
&lt;/code&gt;&lt;/pre&gt;
 
&lt;p&gt;Is this the correct list?  I am unsure because the prototype of *er_get_type()* has *int ** for the type field whereas the &lt;em&gt;ei.h&lt;/em&gt; file defines &lt;em&gt;char&lt;/em&gt; the above constants.&lt;/p&gt;
 
&lt;p&gt;NOTE: There are other 'constants' used in the 'erl_interface' package that aren't listed here.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1492849/rhythmbox-how-do-i-access-the-rating-field-of-a-track-through-a-python</id> 
        <title type="text">Rhythmbox: how do I access the 'rating' field of a track through a Python?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="python"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="rhythmbox"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1492849/rhythmbox-how-do-i-access-the-rating-field-of-a-track-through-a-python" /> 
        <published>2009-09-29T14:18:47Z</published> 
        <updated>2009-09-29T16:27:19Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I would like the capability to get/set the rating associated with a specific track through a Python. How do I achieve this?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1427700/erlang-erlide-what-are-the-compile-options-supported</id> 
        <title type="text">Erlang erlIDE: what are the -compile options supported?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="erlang"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="eclipse"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="erlide"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="compiler"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1427700/erlang-erlide-what-are-the-compile-options-supported" /> 
        <published>2009-09-15T14:56:19Z</published> 
        <updated>2009-09-28T20:30:29Z</updated> 
        <summary type="html"> 
            &lt;p&gt;I've been trying to get erlIDE to work with -compile options e.g.&lt;/p&gt;
 
&lt;blockquote&gt;
  &lt;p&gt;-compile('S').  % Generate 'assembler' listing&lt;/p&gt;
&lt;/blockquote&gt;
 
&lt;p&gt;to no avail.  What I am doing wrong?&lt;/p&gt;
 
&lt;p&gt;NOTE: I have also tried setting 'project specific' options for the compiler with no success.&lt;/p&gt;
 
&lt;p&gt;EDIT: could it be that 'erlc' is invoked and forced to generate a 'beam' and thus disregards orders to generate 'assembler' output?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
<entry> 
    <id>http://stackoverflow.com/questions/1484440/saving-passwords-inside-an-application/1484495#1484495</id> 
    <title type="text">Answer by Jean-Lou Dupont for Saving passwords inside an application </title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1484440/saving-passwords-inside-an-application/1484495#1484495" /> 
    <published>2009-09-27T21:12:22Z</published>   
    <updated>2009-09-27T21:12:22Z</updated> 
    <summary type="html">&lt;p&gt;What about MySQL or SQLite?  Hash the password and store them in a persistent database, no?&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1483687/reducing-size-of-user-avatars-creating-thumbnails/1483991#1483991</id> 
    <title type="text">Answer by Jean-Lou Dupont for Reducing size of user avatars? - creating thumbnails.</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1483687/reducing-size-of-user-avatars-creating-thumbnails/1483991#1483991" /> 
    <published>2009-09-27T17:19:05Z</published>   
    <updated>2009-09-27T17:19:05Z</updated> 
    <summary type="html">&lt;p&gt;Isn't Google AppEngine fitted with a subset of PIL? There is the 'resize' function that could be use... and best of all, you are getting a free quota!&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1483830/python-script-to-find-instances-of-a-set-of-strings-in-a-set-of-files/1483979#1483979</id> 
    <title type="text">Answer by Jean-Lou Dupont for Python Script to find instances of a set of strings in a set of files</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1483830/python-script-to-find-instances-of-a-set-of-strings-in-a-set-of-files/1483979#1483979" /> 
    <published>2009-09-27T17:13:07Z</published>   
    <updated>2009-09-27T17:13:07Z</updated> 
    <summary type="html">&lt;p&gt;You should consider using &lt;a href=&quot;http://www.yaml.org/&quot; rel=&quot;nofollow&quot;&gt;YAML&lt;/a&gt;: easy to use, human readable.&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1483429/how-to-print-error-of-python-simple-question/1483488#1483488</id> 
    <title type="text">Answer by Jean-Lou Dupont for How to print error of python - simple question</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1483429/how-to-print-error-of-python-simple-question/1483488#1483488" /> 
    <published>2009-09-27T12:19:27Z</published>   
    <updated>2009-09-27T12:19:27Z</updated> 
    <summary type="html">&lt;pre&gt;&lt;code&gt;except Exception,e: print str(e)
&lt;/code&gt;&lt;/pre&gt;
</summary> 
</entry> 
    <entry> 
        <id>http://stackoverflow.com/questions/1480110/linux-how-much-data-can-be-passed-as-command-line-arguments</id> 
        <title type="text">Linux: how much data can be passed as command line arguments?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1480110/linux-how-much-data-can-be-passed-as-command-line-arguments" /> 
        <published>2009-09-26T00:47:41Z</published> 
        <updated>2009-09-26T08:17:57Z</updated> 
        <summary type="html"> 
            &lt;p&gt;How many bytes can be sent as command-line argument when spawning a process under Linux?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
<entry> 
    <id>http://stackoverflow.com/questions/1479556/observer-over-a-network/1479626#1479626</id> 
    <title type="text">Answer by Jean-Lou Dupont for Observer over a network</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1479556/observer-over-a-network/1479626#1479626" /> 
    <published>2009-09-25T21:15:29Z</published>   
    <updated>2009-09-25T21:15:29Z</updated> 
    <summary type="html">&lt;p&gt;This sounds like a perfect job for an Erlang system ... or maybe use an AMCQ client like RabbitMQ, no?&lt;/p&gt;
</summary> 
</entry> 
    <entry> 
        <id>http://stackoverflow.com/questions/1478831/erlang-unix-domain-socket-support</id> 
        <title type="text">erlang: UNIX domain socket support?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="sockets"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="erlang"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1478831/erlang-unix-domain-socket-support" /> 
        <published>2009-09-25T18:19:06Z</published> 
        <updated>2009-09-25T20:19:39Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Is there a way to access UNIX domain sockets (e.g. /var/run/dbus/system_bus_socket ) directly from Erlang &lt;strong&gt;without&lt;/strong&gt; resorting to a third-party driver?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1478975/unix-domain-socket-is-there-such-a-thing-as-a-busy-signal</id> 
        <title type="text">UNIX domain socket:  is there such a thing as a &quot;busy&quot; signal?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="sockets"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1478975/unix-domain-socket-is-there-such-a-thing-as-a-busy-signal" /> 
        <published>2009-09-25T18:46:58Z</published> 
        <updated>2009-09-25T19:04:15Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Can a &lt;em&gt;Client&lt;/em&gt; pushing data through a UNIX domain socket ( AF_UNIX type ) be signaled &lt;em&gt;busy&lt;/em&gt; if the receiving end cannot cope with the load?&lt;/p&gt;
 
&lt;p&gt;OR&lt;/p&gt;
 
&lt;p&gt;Must there be a Client-Server protocol on top of the socket to handle flow control?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1478360/erlang-is-there-an-api-to-epmd</id> 
        <title type="text">Erlang: is there an API to 'epmd' ?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="erlang"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="epmd"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1478360/erlang-is-there-an-api-to-epmd" /> 
        <published>2009-09-25T16:42:25Z</published> 
        <updated>2009-09-25T18:39:16Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Is there a way to query the name table that epmd daemon manages?&lt;/p&gt;
 
&lt;p&gt;The &lt;em&gt;nodes()&lt;/em&gt; function isn't very helpful on that front.&lt;/p&gt;
 
&lt;p&gt;NOTE: I am looking for an API &lt;strong&gt;aside&lt;/strong&gt; from parsing the output generated through stdout.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1477174/dbus-is-there-such-a-thing-as-a-dbus-sniffer</id> 
        <title type="text">Dbus:  is there such a thing as a &quot;Dbus sniffer&quot; ?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="dbus"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="monitor"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1477174/dbus-is-there-such-a-thing-as-a-dbus-sniffer" /> 
        <published>2009-09-25T13:03:56Z</published> 
        <updated>2009-09-25T17:13:45Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Is there such a thing as a &quot;Dbus sniffer&quot; ?&lt;/p&gt;
 
&lt;p&gt;I would like to &quot;sniff&quot; all (or part) of the messages transiting on Dbus.&lt;/p&gt;
 
        </summary> 
    </entry> 
    
    <entry> 
        <id>http://stackoverflow.com/questions/1474538/cron-api-is-there-such-a-thing</id> 
        <title type="text">Cron API: is there such a thing?</title> 
        <category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="linux"/><category scheme="http://stackoverflow.com/feeds/user/171461/tags" term="cron"/> 
        <author><name>Jean-Lou Dupont</name></author> 
        <link rel="alternate" href="http://stackoverflow.com/questions/1474538/cron-api-is-there-such-a-thing" /> 
        <published>2009-09-24T22:36:14Z</published> 
        <updated>2009-09-24T23:01:01Z</updated> 
        <summary type="html"> 
            &lt;p&gt;Is there such a thing as a Cron API?&lt;/p&gt;
 
&lt;p&gt;I mean, is there a programmatic way of adding/removing Cron jobs without stepping onto Cron's toes?&lt;/p&gt;
 
        </summary> 
    </entry> 
    
<entry> 
    <id>http://stackoverflow.com/questions/1463470/interfacing-erlang-application-with-php/1463549#1463549</id> 
    <title type="text">Answer by Jean-Lou Dupont for interfacing erlang application with php</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1463470/interfacing-erlang-application-with-php/1463549#1463549" /> 
    <published>2009-09-23T01:38:45Z</published>   
    <updated>2009-09-23T01:38:45Z</updated> 
    <summary type="html">&lt;p&gt;Erlang is excellent at socket I/O:  maybe you could use a pipe of some sort?&lt;/p&gt;
 
&lt;p&gt;This would be more direct than through another WEB server layer for sure.&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1453296/do-robots-crawl-iframes/1453439#1453439</id> 
    <title type="text">Answer by Jean-Lou Dupont for Do robots crawl iframes?</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1453296/do-robots-crawl-iframes/1453439#1453439" /> 
    <published>2009-09-21T08:34:06Z</published>   
    <updated>2009-09-21T08:34:06Z</updated> 
    <summary type="html">&lt;p&gt;If there is an href/src link somewhere on an &lt;strong&gt;indexed&lt;/strong&gt; (i.e. &lt;em&gt;crawled&lt;/em&gt;) HTML/XHTML page, it will get indexed. Whether or not the page is presented to the user via an iFrame is irrelevant.&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/426765/c-libraries-for-parsing-erlang-binaries/1452494#1452494</id> 
    <title type="text">Answer by Jean-Lou Dupont for C libraries for parsing Erlang binaries?</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/426765/c-libraries-for-parsing-erlang-binaries/1452494#1452494" /> 
    <published>2009-09-21T01:18:22Z</published>   
    <updated>2009-09-21T01:18:22Z</updated> 
    <summary type="html">&lt;p&gt;I've crafted my own: &lt;a href=&quot;http://code.google.com/p/epapi/&quot; rel=&quot;nofollow&quot;&gt;EPAPI&lt;/a&gt; (Erlang Port API) in C/C++. Very easy to use and I provide a Debian repo for easy updates.&lt;/p&gt;
 
&lt;h2&gt;Example&lt;/h2&gt;
 
&lt;pre&gt;&lt;code&gt; PktHandler *ph = new PktHandler();
 MsgHandler *mh = new MsgHandler(ph);
 
 //Register a message type
 // {echo, {Counter}}
 mh-&amp;gt;registerType(1, &quot;echo&quot;, &quot;l&quot; );
 
 //Wait for a message
 Msg *m;
 result = mh-&amp;gt;rx(&amp;amp;m);
 
 //Verify return code
 if (result) {
    //handle error
    printf(&quot;ERROR, message: %s&quot;, mh-&amp;gt;strerror());
    // ...
 }
&lt;/code&gt;&lt;/pre&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/257245/message-passing-concurrency-library-for-c/1452477#1452477</id> 
    <title type="text">Answer by Jean-Lou Dupont for Message Passing Concurrency Library for C?</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/257245/message-passing-concurrency-library-for-c/1452477#1452477" /> 
    <published>2009-09-21T01:08:19Z</published>   
    <updated>2009-09-21T01:08:19Z</updated> 
    <summary type="html">&lt;p&gt;I've got just the thing for you:  &lt;a href=&quot;http://code.google.com/p/litm/&quot; rel=&quot;nofollow&quot;&gt;LITM&lt;/a&gt; (Lightweight Inter-thread Messaging) written in C for Linux.&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/908718/why-cant-i-start-a-named-erlang-node-in-windows/1452465#1452465</id> 
    <title type="text">Answer by Jean-Lou Dupont for Why can't I start a named Erlang node in Windows?</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/908718/why-cant-i-start-a-named-erlang-node-in-windows/1452465#1452465" /> 
    <published>2009-09-21T01:03:32Z</published>   
    <updated>2009-09-21T01:03:32Z</updated> 
    <summary type="html">&lt;p&gt;1) You need to make sure you are not using an already registered name (of course): this include any name already claimed by Erlang already&lt;/p&gt;
 
&lt;p&gt;2) If you are starting on the same machine but under different user, make sure your cookies are the same&lt;/p&gt;
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver/1513884#1513884</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver/1513884#1513884" /> 
    <published>2009-10-03T19:58:06Z</published>   
    <updated>2009-10-03T19:58:06Z</updated> 
    <summary type="html">@Lennart:  THANKS!!! that must have been my problem!</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513640#1513640</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513640#1513640" /> 
    <published>2009-10-03T15:24:04Z</published>   
    <updated>2009-10-03T15:24:04Z</updated> 
    <summary type="html">@kaizer: many thanks for all your efforts.  I discovered the SAX parser thanks to this post and it looks like I'll be able to manage building my state-machine based parser neatly with this approach.  (Can you tell I am an XML-newbie ? ;-)</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver/1513884#1513884</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver/1513884#1513884" /> 
    <published>2009-10-03T15:04:55Z</published>   
    <updated>2009-10-03T15:04:55Z</updated> 
    <summary type="html">strange... the last time I uploaded an egg the way you describe, it was tagged with the python version used to make it... and then if I tried &lt;i&gt;easy_install&lt;/i&gt; on it with a different Python version, it wouldn't work...  Could you provide an explanation please?</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513621#1513621</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513621#1513621" /> 
    <published>2009-10-03T12:46:01Z</published>   
    <updated>2009-10-03T12:46:01Z</updated> 
    <summary type="html">@kaizer:  example, please please?</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513640#1513640</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513640#1513640" /> 
    <published>2009-10-03T12:43:23Z</published>   
    <updated>2009-10-03T12:43:23Z</updated> 
    <summary type="html">@kaizer: So in effect it is like working with the subset of the document each time the for-loop is entered after the element.clear() ?</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513621#1513621</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513621#1513621" /> 
    <published>2009-10-03T12:34:33Z</published>   
    <updated>2009-10-03T12:34:33Z</updated> 
    <summary type="html">... because that's what happens with &amp;quot;iterparse&amp;quot;...</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513621#1513621</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513621#1513621" /> 
    <published>2009-10-03T12:33:37Z</published>   
    <updated>2009-10-03T12:33:37Z</updated> 
    <summary type="html">so if I put a &amp;quot;yield&amp;quot; statement in the for-loop {e.g. for (event,node) in events: yield (event, node)} PullDom won't restart at the beginning next time I enter the for-loop ?
</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver/1513605#1513605</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1512644/python-pypi-what-is-your-process-for-releasing-packages-for-different-python-ver/1513605#1513605" /> 
    <published>2009-10-03T12:23:29Z</published>   
    <updated>2009-10-03T12:23:29Z</updated> 
    <summary type="html">@ned: many thanks for your contribution.  I am on Linux and I do not have a Windows box handy anymore.</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513604#1513604</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1513592/python-is-there-an-xml-parser-implemented-as-a-generator/1513604#1513604" /> 
    <published>2009-10-03T12:21:52Z</published>   
    <updated>2009-10-03T12:21:52Z</updated> 
    <summary type="html">that's what I want... I don't mind having to &amp;quot;react&amp;quot; to events such as &amp;quot;start tag&amp;quot; etc.</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file" /> 
    <published>2009-09-30T15:44:31Z</published>   
    <updated>2009-09-30T15:44:31Z</updated> 
    <summary type="html">@hacker: thanks!</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498244#1498244</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498244#1498244" /> 
    <published>2009-09-30T14:28:19Z</published>   
    <updated>2009-09-30T14:28:19Z</updated> 
    <summary type="html">Doesn't account for the relative path hierarchy contained in the &lt;i&gt;sub&lt;/i&gt; makefiles.</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498399#1498399</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498399#1498399" /> 
    <published>2009-09-30T14:27:20Z</published>   
    <updated>2009-09-30T14:27:20Z</updated> 
    <summary type="html">Tried this but it does not work with the default command launch &lt;i&gt;make&lt;/i&gt; : it complains that the target &lt;b&gt;all&lt;/b&gt; isn't specified ;-(</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498232#1498232</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498232#1498232" /> 
    <published>2009-09-30T14:26:04Z</published>   
    <updated>2009-09-30T14:26:04Z</updated> 
    <summary type="html">It seems that having a &lt;b&gt;%&lt;/b&gt; target proves useful to helping solve my problem... the trouble is that the implicit target &lt;i&gt;all&lt;/i&gt;  (when just invoking &lt;i&gt;make&lt;/i&gt; without parameters) does not get processed... how do I go about solving this?</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498232#1498232</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498232#1498232" /> 
    <published>2009-09-30T14:19:52Z</published>   
    <updated>2009-09-30T14:19:52Z</updated> 
    <summary type="html">But I do not want to have to specify all the supported target in this 'top level' makefile: I want to pass along the targets from the command-line down to the &lt;i&gt;sub&lt;/i&gt; makefiles... How do I achieve this?</summary> 
</entry> 
<entry> 
    <id>http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498232#1498232</id> 
    <title type="text">Comment by Jean-Lou Dupont</title> 
    <author><name>Jean-Lou Dupont</name></author> 
    <link rel="alternate" href="http://stackoverflow.com/questions/1498213/make-hierarchical-make-file/1498232#1498232" /> 
    <published>2009-09-30T14:15:10Z</published>   
    <updated>2009-09-30T14:15:10Z</updated> 
    <summary type="html">what does the $(BUILD) variables stand for?  Is it contextual to make itself &lt;i&gt;or&lt;/i&gt; am I expected to specify it?</summary> 
</entry> 
</feed>
"""

    import os
    import sys
    from xml.sax import parseString
    from xml.sax.handler import ContentHandler 

    sr=simpleReceptor()
    feedHandler=rssHandler(sr)

    parseString(testFeed, feedHandler)

    print feedHandler.header
