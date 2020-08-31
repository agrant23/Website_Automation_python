#Test_Cases_3

import unittest
import string
import random
import time
import Secure 
from Yahoo_Page_3 import *


class HomePageSetup(unittest.TestCase):

    def random_password_generator(self, password_len):                  #self is needed in paramaters and to call the function needs self.function_name
        excluded_password_characters = ['\n','\t','\r','\x0b','\x0c']  
        for char in excluded_password_characters:
            password_characters = string.printable.replace(char,'')
        password = ''.join(random.choice(password_characters) for x in range(password_len))
        return password


    def setUp(self):

        self.driver = webdriver.Chrome(options=options1)
        self.yahoo_page = Yahoo_Page_3(self.driver)

        yahoo_page.load_website("https://www.yahoo.com",self.driver)
                
        #after loading an extension it opens a new tab, so I tab back to yahoo tab
        yahoo_page.switch_to_tab(self.driver)

        yahoo_page.sign_in_button_click(self.driver)

        user_name_field = yahoo_page.get_username_field(self.driver)
        yahoo_page.input_string(Secure.yahoo_username, user_name_field)

        user_name_button = yahoo_page.username_next_button(self.driver)
        yahoo_page.click(user_name_button)

        password_field = yahoo_page.get_password_field(self.driver)
        yahoo_page.input_string(Secure.yahoo_password,password_field)

        password_button = yahoo_page.password_next_button(self.driver)
        yahoo_page.click(password_button)

        yahoo_page.tab_off_pop_up(self.driver)

        profile_menu = yahoo_page.profile_menu(self.driver)
        yahoo_page.click(profile_menu)

        profile_settings = yahoo_page.profile_menu_settings(self.driver)
        yahoo_page.click(profile_settings)

        account_secuirty_tab = yahoo_page.account_security_tab(self.driver)
        yahoo_page.click(account_secuirty_tab)

        change_password = yahoo_page.change_password_link(self.driver)
        yahoo_page.click(change_password)

#class error_message_tests(HomePageSetup):

    def test_short_password_error_message(self):
        """ 
        Confirm the password is one character short of the clients required password length
        for the error data criteria. Confirm the data for the error exists when the password
        is entered and the resulting error text matches the output text. 

        acceptance criteria   
        --------------------
        -When a password that is too short is entered data error exists
        -When a password that is too short is entered the error text explaining this appears
        """

        yahoo_page = self.yahoo_page
        
        short_password = self.random_password_generator(6)
        new_password_field = yahoo_page.get_new_password_field(self.driver)
        yahoo_page.input_string(short_password,new_password_field)
        
        #tab to the Confirm Password field, to load the error message
        yahoo_page.tab_to_next_field(self.driver)    

        password_status = yahoo_page.password_error_message(self.driver)

        self.assertEqual(password_status.get_attribute('data-error'),"WEAK_PASSWORD")  
        self.assertEqual(password_status.text,"Your password is too easy to guess, try making it longer.")


    def test_long_password_error_message(self):
        """ 
        Confirm the password is at the clients required password length for the error data criteria.
        Confirm the data for the error does not exists when the password is entered and there
        is no resulting error text.

        acceptance criteria   
        --------------------
        -When a password that meets the required length is entered data error does not exists
        -When a password that meets the required lenght is entered there is no error text
        """
        
        yahoo_page = Yahoo_Page_3(self.driver)
        
        long_password = self.random_password_generator(8)
        new_password_field = yahoo_page.get_new_password_field(self.driver)
        yahoo_page.input_string(long_password,new_password_field)
        
        yahoo_page.tab_to_next_field(self.driver) 
        
        password_status = yahoo_page.password_error_message(self.driver)

        self.assertEqual(password_status.get_attribute('data-error'),"")
        self.assertEqual(password_status.text,"")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__": unittest.main()