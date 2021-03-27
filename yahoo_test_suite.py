import unittest
import test_cases as test_case


suite = unittest.TestSuite()
suite.addTest(test_case.ErrorMessagePasswords(
    "test_short_password_error_message"))
suite.addTest(test_case.ErrorMessagePasswords(
    "test_moderate_password_error_message"))
suite.addTest(test_case.ErrorMessagePasswords(
    "test_long_password_error_message"))
suite.addTest(test_case.Search("test_cursur_on_search_field"))
suite.addTest(test_case.Search('test_search_page'))
suite.addTest(test_case.DynamicDropDown('test_any_random_tab'))
suite.addTest(test_case.DynamicDropDown('test_any_random_tab'))
suite.addTest(test_case.DynamicDropDown('test_any_random_tab'))
suite.addTest(test_case.LogInLink("test_log_in_link"))
suite.addTest(test_case.PasswordLink("test_change_password_link"))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
