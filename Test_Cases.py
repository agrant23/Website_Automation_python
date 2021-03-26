from selenium import webdriver
import unittest
from yahoo_page import YahooPage
import tools
import settings
import time


class HomePageSetup(unittest.TestCase):

    def setUp(self):
        options = YahooPage.options
        self.driver = webdriver.Chrome(
                                   settings.path_to_webdriver, options=options)
        self.yahoo_page = YahooPage(self.driver)

    def tearDown(self):
        self.driver.quit()


class ErrorMessagePasswords(HomePageSetup):
    
    def random_password(self, password_len):
        excluded_password_chars = ['\n', '\t', '\r', '\x0b', '\x0c']
        return tools.generate_random_string(
            password_len, excluded_password_chars)

    def setUp(self):
        super().setUp()

        self.yahoo_page.login()
        self.yahoo_page.navigate_to_security_tab()
        self.yahoo_page.click_change_password_link()

    def test_short_password_error_message(self):
        """
        Confirm that when the password is 8 characters that the data
        error status is "WEAK_PASSWORD" Confirm the resulting error text
        is "- Your password is too easy to guess."

        acceptance criteria
        --------------------
        -When an 8 character password is entered, the data error status
         and the error text exhibit's this is too short of a password.

        Note
        --------------------
        -Yahoo security will randomly ask to "prove you are not a robot".
         Which, at times, can be responsible for the tests in Error Message
         Passwords class to error. There is not an easy fix for this.
        """
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(5))

        self.assertEqual(yahoo_page.short_password_error_message().
                         get_attribute('data-error'), "WEAK_PASSWORD")
        self.assertEqual(yahoo_page.short_password_error_message().text,
                         "- Your password is too easy to guess.")

    def test_moderate_password_error_message(self):
        """
        Confirm that when the password 9 or 10 characters in length, the
        error data status is "ALMOST_THERE". Confirm the resulting error
        text is "- Almost there".

        acceptance criteria
        --------------------
        -When a password that is between 9 and 10 characters is entered,
         the data error status and the error text exhibit's this is a
         moderate length for the password.
        """
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(9))

        self.assertEqual(yahoo_page.moderate_password_error_message().
                         get_attribute('data-error'), "ALMOST_THERE")
        self.assertEqual(yahoo_page.moderate_password_error_message().text,
                         "- Almost there.")

    def test_long_password_error_message(self):
        """
        Confirm that when the password is 11 characters, the error data
        status is "STRONG_PASSWORD". Confirm the resulting error text is
        "- you did it!".

        acceptance criteria
        --------------------
        -When a password that is 11 characters is entered, the data
         error and error text either does not exist or it exhibits this
         is a password of sufficient length.
        """
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(11))

        self.assertEqual(yahoo_page.long_password_error_message().
                         get_attribute('data-error'), "STRONG_PASSWORD")
        self.assertTrue(yahoo_page.long_password_error_message().text == "" or
                        yahoo_page.long_password_error_message().text == None
                        or yahoo_page.long_password_error_message().text ==
                        "- you did it!", "\n"
                        + yahoo_page.long_password_error_message().text +
                        ' appeared intead of - you did it!')
        #The assertTrue above is necessary due to the error messaging returning
        #an empty string, None or a text.
        #Logic operators do not work within AssertEqual


class Search(HomePageSetup):
    """
    Confirm the cursor is present in the Search field after the yahoo
    home page is opened. After an arbitrary input is given to the search
    field confirm that clicking the search button navigates the user to
    the search page.

    acceptance criteria
    --------------------
    -The cursor is in the search field after the yahoo home page is opened.
    -When the search field is given an input,
     the user is navigated to the search page.
    """
    def test_cursur_on_search_field(self):

        self.assertEqual(
            self.yahoo_page.current_cursor_id(),
            self.yahoo_page.search_field_id())

    def test_search_page(self):

        self.yahoo_page.input_search_field('Kendrick Lamar')
        self.yahoo_page.click_search_button()
        self.assertIn('search', self.driver.current_url,
                      '\nSearch of: ' + self.yahoo_page.search_field_contents()
                      + " is not in the " + self.driver.current_url + " URL")


class DynamicDropDown(HomePageSetup):
    """
    For the Originals drop down menu within yahoo news; ensure that
    clicking on this drop down's options sends the user to the
    correlating site.

    acceptance criteria
    --------------------
    -The title of the Originals drop down options sends the user to the
     given by the provided dictionary.
    """

    def setUp(self):
        super().setUp()
        self.yahoo_page.click_news_link()
        #Maximize is needed to hover over the originals tab in headed mode.
        self.driver.maximize_window()
        self.yahoo_page.hover_over_originals_drop_down()

    def test_any_random_tab(self):
        #Dictionary of option titles and corresponding url.
        dict_option_title_url_block = {'The 360': '360',
                                       'Skullduggery': 'skullduggery',
                                       'Conspiracyland': 'conspiracyland'}
        yahoo_page = self.yahoo_page
        yahoo_page.click_random_option_from_originals_drop_down()
        self.assertIn(dict_option_title_url_block[
            yahoo_page.random_option_title], self.driver.current_url)


class LogInLink(HomePageSetup):

    def test_log_in_link(self):
        """
        Confirm the log in internal link is correct.

        acceptance criteria
        --------------------
        -After clicking the sign in button, the URL has changed to the
         login page.
        """

        self.yahoo_page.click_sign_in_button()
        self.assertIn('login', self.driver.current_url)


class PasswordLink(HomePageSetup):

    def setUp(self):
        super().setUp()

        self.yahoo_page.login()
        self.yahoo_page.navigate_to_security_tab()

    def test_change_password_link(self):
        """
        Confirm the change password internal link is correct.

        acceptance criteria
        --------------------
        -After clicking the change password button,
         the URL has changed to the login page.

        Note
        --------------------
        -Yahoo security will randomly ask to "prove you are not a robot".
         Which, at times, is responsible for this test erroring out.
        """

        self.yahoo_page.click_change_password_link()
        self.assertIn('change-password', self.driver.current_url)


if __name__ == "__main__": unittest.main()
