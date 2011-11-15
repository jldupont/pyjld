#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: tests.py 37 2009-04-03 01:58:16Z jeanlou.dupont $"

import unittest, doctest

def test_suite(*args):

    test = doctest.DocFileSuite(
        "tests.txt",
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE)


    return unittest.TestSuite((test,))



# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    suite = unittest.TestSuite()
    suite.addTest( test_suite() )
    runner = unittest.TextTestRunner()
    runner.run(suite)
