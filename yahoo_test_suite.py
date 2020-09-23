import unittest
from Test_Cases import *


suite = unittest.TestSuite()
suite.addTest(Search("test_cursur_on_search_field"))
suite.addTest(Search('test_search_page'))
suite.addTest(Dynamic_Drop_Down('test_any_random_tab'))
suite.addTest(Dynamic_Drop_Down('test_any_random_tab'))
suite.addTest(Dynamic_Drop_Down('test_any_random_tab'))
suite.addTest(Log_In_Link("test_log_in_link"))
suite.addTest(Password_Link("test_change_password_link"))
suite.addTest(Error_Message_Passwords("test_short_password_error_message"))
suite.addTest(Error_Message_Passwords("test_long_password_error_message"))




if __name__ == "__main__": 
    runner = unittest.TextTestRunner()
    runner.run(suite)