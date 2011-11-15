#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: test_protocol.py 62 2009-04-15 19:05:01Z jeanlou.dupont $"

__all__ = ['',]


import unittest, doctest

def test_suite(*args):

    test = doctest.DocFileSuite(
        "test_protocol.txt",
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
