#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: tests.py 44 2009-04-06 14:21:24Z jeanlou.dupont $"


from pyjld.system.proxy import ProxyBaseClass


class TestProxy(ProxyBaseClass):
    def __init__(self, target):
        ProxyBaseClass.__init__(self, target)
        
def TestTarget(event, *pargs, **kargs):
    print "TestTarget: event[%s] pargs[%s] kargs[%s]" % (event, pargs, kargs)


def tests1():
    """
    >>> p = TestProxy( TestTarget )
    >>> p.event_A()
    TestTarget: event[event_A] pargs[()] kargs[{}]
    >>> p.event_B('p_param1')
    TestTarget: event[event_B] pargs[('p_param1',)] kargs[{}]
    >>> p.event_C(kparam1="kparam1")
    TestTarget: event[event_C] pargs[()] kargs[{'kparam1': 'kparam1'}]
    """
    
# ===========================================================================
# ===========================================================================



class TestEventSource(object):
    def __init__(self):
        self.table = {}
    
    def attachEventA(self, callback):
        self.table['a'] = callback

    def attachEventB(self, callback):
        self.table['b'] = callback

    def __call__(self, event, *pargs, **kargs):
        return self.table[event](*pargs, **kargs)
        

class TestProxy2(ProxyBaseClass):
    
    liste = [('attachEventA', 'a'),('attachEventB','b')]
    
    def __init__(self, target):
        ProxyBaseClass.__init__(self, target)
        self.source = TestEventSource()
        self.wireEventSources(self.source, self.liste)
        
    def generate(self, event, *pargs, **kargs):
        return self.source(event, *pargs, **kargs)



def tests2():
    """
    >>> p2 = TestProxy2( TestTarget )
    >>> p2.generate('a')
    TestTarget: event[event_a] pargs[()] kargs[{}]
    >>> p2.generate('a', "param1")
    TestTarget: event[event_a] pargs[('param1',)] kargs[{}]
    >>> p2.generate('b', kparam1="kparam1")
    TestTarget: event[event_b] pargs[()] kargs[{'kparam1': 'kparam1'}]
    """

import doctest
doctest.testmod()
