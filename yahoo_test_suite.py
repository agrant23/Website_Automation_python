import unittest
from Test_Cases import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Test_Sign_In_Link("test_sign_in_link"))
    suite.addTest(Test_Password_Link("test_change_password_link"))
    suite.addTest(Error_Message_Tests("test_short_password_error_message"))
    suite.addTest(Error_Message_Tests("test_long_password_error_message"))
    return suite


if __name__ == "__main__": 
    runner = unittest.TextTestRunner()
    runner.run(suite())