import unittest
from testsuite.test_validators import TestUserAuthorizationValidator

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUserAuthorizationValidator))

    return test_suite

if __name__ == '__main__':
    all_tests = suite()
    runner = unittest.TextTestRunner()
    runner.run(all_tests)


''' 
execute this cmd: python3 -m unittest -v testsuite/run_all_tests.py

'''