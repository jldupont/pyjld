#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: tests.py 33 2009-04-02 18:47:23Z jeanlou.dupont $"

import unittest, doctest

def test_suite(*args):

    test = doctest.DocFileSuite(
        "tests.txt",
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)


    return unittest.TestSuite((test,))



from pyjld.system.command import BaseCmd

class TestCmd(BaseCmd):
    
    def __init__(self):
        BaseCmd.__init__(self)
        
    def cmd_start(self, *pargs, **kwargs):
        print "TestCmd.cmd_start"

    def cmd_stop(self, *pargs, **kwargs):
        print "TestCmd.cmd_stop"


class TestsBaseCmd(unittest.TestCase):
    
    def setUp(self):
        self.cmd = TestCmd()
    
    def tearDown(self):
        pass

    def testCmdList(self):
        liste = ['start','stop']
        
        for command in liste:                
            result = self.cmd.safe_validateCommand(command)
            self.assertEqual(result, True)



# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    suite = unittest.TestSuite()
    suite.addTest( test_suite() )
    suite.addTest( unittest.TestLoader().loadTestsFromTestCase( TestsBaseCmd ) )
    runner = unittest.TextTestRunner()
    runner.run(suite)
