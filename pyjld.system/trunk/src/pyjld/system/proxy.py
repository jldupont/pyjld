#!/usr/bin/env python
""" 
pyjld.system.proxy
"""
__author__  = "Jean-Lou Dupont"
__fileid    = "$Id: proxy.py 44 2009-04-06 14:21:24Z jeanlou.dupont $"


__all__ = ['ProxyCallback', 'ProxyBaseClass']

        
class ProxyCallback(object):
    """ 
    Proxy callback helper class
    """
    __all__ = ['callback','event']
    
    def __init__(self, callback, event):
        self.callback = callback
        self.event    = event

    def __call__(self, *pargs, **kargs):
        return self.callback( self.event, *pargs, **kargs)




class ProxyBaseClass(object):
    """ 
    Proxy base class

    This class serves as a 'proxy' between 
    events (method calls) and a receiving target. 
    
    The events are trapped through the use of the 
    magic method __getattr__: a prefix can
    be configured for these methods.    
    """
    def __init__(self, target, prefix = 'event_'):
        self.target = target
        self.prefix = prefix
               
    def __getattr__(self, name):
        """ Traps the events (method calls)
        
            Performs verification against the configured prefix.
        """
        if not name.startswith(self.prefix):
            raise AttributeError('ProxyBaseClass: name[%s] undefined' % name)
        
        return ProxyCallback(self.target, event=name)

    def wireEventSources(self, source, liste):
        """ Wires the event sources to this proxy
        
            If this class is used to contain an object which
            generates events, the said events can be configured
            through this method to point to the proxy.
            
            The parameter 'liste' is defined:
                [(attachMethodName1, eventName), (attachMethodName2, eventName), ...]
        """
        for attachMethodName, eventName in liste:
            # retrieve attach method
            methodInstance  = self._getMethodInstance(source, attachMethodName)
            
            # generate event method instance local to this proxy
            eventMethodName = self.prefix + eventName
            eventMethodInstance = self._getMethodInstance(self, eventMethodName)
            
            # wire the event source to the proxy
            try:
                methodInstance( eventMethodInstance )
            except:
                raise RuntimeError('ProxyBaseClass: exception whilst trying to wire source[%s] with event[%s]' % (type(source), eventName) ) 
            
        
    def _getMethodInstance(self, source, name):
        try:
            methodInstance = getattr(source, name)
        except:
            raise RuntimeError("ProxyBaseClass: can't find attach method[%s]" % name)
        
        return methodInstance
