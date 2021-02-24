"""
******** Test Suite for all test_cases cases ************
"""
import unittest
from test_cases.TestHomePageLinks import VerifyHomePageLinks

verify_all_links = unittest.TestLoader().loadTestsFromTestCase(VerifyHomePageLinks)
suite = unittest.TestSuite(verify_all_links)
unittest.TextTestRunner(verbosity=2).run(suite)
