#yahoo_test_suite_2

import unittest
from Test_Cases import *

test_loader = unittest.TestLoader()

passwor_error_test = test_loader.loadTestsFromTestCase(Search)
passwor_error_test = test_loader.loadTestsFromTestCase(Dynamic_Drop_Down)
sign_in_link_test = test_loader.loadTestsFromTestCase(Sign_In_Link)
password_link_test = test_loader.loadTestsFromTestCase(Password_Link)
passwor_error_test = test_loader.loadTestsFromTestCase(Error_Message_Passwords)

test_suite = unittest.TestSuite([sign_in_link_test,password_link_test,passwor_error_test])

unittest.TextTestRunner().run(test_suite)