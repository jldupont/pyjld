#!/usr/bin/env python
"""
pyjld.amqp.client_0_8.layers.stack
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: stack.py 69 2009-04-17 18:49:17Z jeanlou.dupont $"

__all__ = ['',]

from pyjld.amqp.client_0_8.serialization import AMQPWriter, AMQPReader


class AMQPStack(object):

    def __init__(self):
        self._stack = []
        

    def append(self, fragment):
        self._stack.append( fragment )
        
        
    def bottomUpGenerator(self):
        for fragment in self._stack:
            yield fragment

        
    def topDownGenerator(self):
        for fragment in reversed(self._stack):
            yield fragment
    
            
    def writeProcess(self, fragments):
        """
        Perform the ``write`` process
        
        Writes each fragment bottom-up
        to the output stream
        """
        output = AMQPWriter()
        
        #HEADERS
        for fragment in self.bottomUpGenerator():
            fragment.writeHeader(output)
            

            #BODY
        fragment.writeBody(output)
            

                #FOOTERS
        for fragment in self.topDownGenerator():
            fragment.writeFooter(output)
            
        return output

    
    def readProcess(self, stream):
        """
        Perform the ``read`` process
        
        Presents the stream bottom-up 
        to each protocol of the stack
        """
        fragments = []
        
        #HEADERS
        for fragment in self.bottomUpGenerator():
            fragment.writeHeader(output)
            

            #BODY
        fragment.writeBody(output)
            

                #FOOTERS
        for fragment in self.topDownGenerator():
            fragment.writeFooter(output)
            
        return output


        
        