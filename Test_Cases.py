#Test_Cases_3

import unittest
import string
import random
import time
import Secure 
from Yahoo_Page import *


class HomePageSetup(unittest.TestCase):

    def random_password(self, password_len):                
        excluded_password_characters = ['\n','\t','\r','\x0b','\x0c']  
        for char in excluded_password_characters:
            password_characters = string.printable.replace(char,'')
            password = ''.join(random.choice(password_characters) for x in range(password_len))
        return password

    def setUp(self):

        self.driver = webdriver.Chrome(options=options)       
        self.yahoo_page = Yahoo_Page(self.driver)
        yahoo_page = self.yahoo_page

        yahoo_page.load_website("https://www.yahoo.com")
                
        #after loading an extension it opens a new tab, so I tab back to yahoo tab
        yahoo_page.switch_to_tab()
    
    def tearDown(self):
        self.driver.quit()

class Test_Sign_In_Link(HomePageSetup):

    def test_sign_in_link(self):

        yahoo_page = self.yahoo_page

        yahoo_page.click_sign_in_button()
        yahoo_page.open_login_page()

        self.assertTrue('login' in self.driver.title) 

class Test_Password_Link(HomePageSetup):

    def setUp(self):
        super().setUp()

        yahoo_page = self.yahoo_page

        yahoo_page.click_sign_in_button()
        yahoo_page.input_username_field(Secure.yahoo_username) 
        yahoo_page.click_username_next_button()

        yahoo_page.input_password_field(Secure.yahoo_password)
        yahoo_page.click_password_next_button()

        yahoo_page.tab_off_pop_up()

        yahoo_page.click_profile_menu()
        yahoo_page.click_profile_menu_settings()
        yahoo_page.click_account_security_tab()
        yahoo_page.click_change_password_link()

    def test_change_password_link(self):

        self.assertIn('change-password' , self.driver.current_url)

class Error_Message_Tests(Test_Password_Link):

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