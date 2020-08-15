#Test_Cases_3

import unittest
import string
import random
import time
from Yahoo_Page import *


class HomePageSetup(unittest.TestCase):         #Template class         

    def random_password(self, password_len):                  #self is needed in paramaters and to call the function needs self.function_nam
        excluded_password_characters = ['\n','\t','\r','\x0b','\x0c']  
        for char in excluded_password_characters:
            password_characters = string.printable.replace(char,'')
            password = ''.join(random.choice(password_characters) for x in range(password_len))
        return password

    def setUp(self):

        self.driver = webdriver.Chrome(options=options)  
        self.yahoo_page = Yahoo_Page(self.driver)      

    def tearDown(self):
        self.driver.quit()

class Test_Sign_In_Link(HomePageSetup):

    def test_sign_in_link(self):
        """ 
        Confirm the sign in or login internal link is correct 

        acceptance criteria   
        --------------------
        -After clicking the sign in button the link's URL is on the login page 
        """

        self.yahoo_page.click_sign_in_button()
        self.assertIn('login', self.driver.current_url) 

class Test_Password_Link(HomePageSetup):

    def setUp(self):
        super().setUp()

        self.yahoo_page.login()
        self.yahoo_page.navigate_to_security_tab()

    def test_change_password_link(self):
        """ 
        Confirm the sign in or login internal link is correct 

        acceptance criteria   
        --------------------
        -After clicking the sign in button the link's URL is on the login page 
        """

        self.yahoo_page.click_change_password_link()
        self.assertIn('change-password', self.driver.current_url)

class Error_Message_Tests(HomePageSetup):

    def setUp(self):
        super().setUp()

        self.yahoo_page.login()
        self.yahoo_page.navigate_to_security_tab()
        self.yahoo_page.click_change_password_link() 

    def test_short_password_error_message(self):
        """ 
        Confirm the entered password is one character short of required minimum length.
        Confirm error data pops up when the short password is entered.
        Confirm the resulting error text matches the current sentence/wording. 

        acceptance criteria   
        --------------------
        -When a password that is too short is entered data error exists,
        the error text appears and is the same as it is now 08/08/2020
        """
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(6))
        
        #tab to the Confirm Password field, to load the error message
        yahoo_page.tab_to_next_field()   

        self.assertEqual(yahoo_page.password_error_message().get_attribute('data-error'),"WEAK_PASSWORD")  
        self.assertEqual(yahoo_page.password_error_message().text,"Your password is too easy to guess, try making it longer.")


    def test_long_password_error_message(self):
        """ 
        Confirm the entered password is one character longer than the required minimum length.
        Confirm error data does not pop up when the long password is entered.
        Confirm there is no error text popping up 

        acceptance criteria   
        --------------------
        -When a password that is too long is entered data error does not exist and
        the error text does not appears
        """
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(8))
        
        yahoo_page.tab_to_next_field()

        self.assertEqual(yahoo_page.password_error_message().get_attribute('data-error'),"")
        self.assertEqual(yahoo_page.password_error_message().text,"")

if __name__ == "__main__": unittest.main()