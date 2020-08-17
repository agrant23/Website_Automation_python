
import unittest
import time
from Yahoo_Page import *
from Tools import *

class HomePageSetup(unittest.TestCase):         #Template class         

    def random_password(self, password_len): 
        excluded_password_chars = ['\n','\t','\r','\x0b','\x0c']                
        return Tools().generate_random_string(excluded_password_chars, password_len)
        
    def setUp(self):

        self.driver = webdriver.Chrome(options=options)  
        self.yahoo_page = Yahoo_Page(self.driver)      

    def tearDown(self):
        self.driver.quit()


class Search(HomePageSetup):
    """
    Confirm the cursor is present in the Search field after the yahoo home page is opened.
    After an arbitrary input is given to the search field confirm that clicking the search icon navigates
    the user to the search page.  There are at least three links in the search page that directly correlate 
    to the search input.       

    acceptance criteria   
    --------------------
    -The cursur is in the search field after the yahoo home page is opened.
    -When the search field is given an input, the user is navigated to the search page.
    -At least three correlating links to the search input appear in the search page
    """
    def test_cursur_on_search_field(self):

        #I know I need an action here due to the definition of what a test is. However the test relies on nothing happening; or the cursor being where it 'should' be after yahoo home page open's
        self.assertEqual(self.yahoo_page.current_cursor_id(), self.yahoo_page.search_field_id())

    def test_search_page(self):

        yahoo_page = self.yahoo_page
        
        yahoo_page.input_search_field('Kendrick Lamar')
        yahoo_page.click_search_button()
        self.assertIn('login', self.driver.current_url) #,
            #'\nLocation: ' + yahoo_page.location_field_contents() + '\nRewards: ' + yahoo_page.rewards_field_contents())


class Sign_In_Link(HomePageSetup):

    def test_sign_in_link(self):
        """ 
        Confirm the sign in or login internal link is correct 

        acceptance criteria   
        --------------------
        -After clicking the sign in button the browser's URL is on the login page 
        """

        self.yahoo_page.click_sign_in_button()
        self.assertIn('login', self.driver.current_url) 


class Password_Link(HomePageSetup):

    def setUp(self):
        super().setUp()

        self.yahoo_page.login()
        self.yahoo_page.navigate_to_security_tab()


    def test_change_password_link(self):
        """ 
        Confirm the sign in or login internal link is correct 

        acceptance criteria   
        --------------------
        -After clicking the sign in button the browser's URL is on the login page 
        """

        self.yahoo_page.click_change_password_link()
        self.assertIn('change-password', self.driver.current_url)


class Error_Message_Passwords(HomePageSetup):

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
        yahoo_page.tab_to_next_field()   #tab to the Confirm Password field, to load the error message

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
        yahoo_page.tab_to_next_field()      #tab to the Confirm Password field, to load the error message

        self.assertEqual(yahoo_page.password_error_message().get_attribute('data-error'),"")
        self.assertEqual(yahoo_page.password_error_message().text,"")

if __name__ == "__main__": unittest.main()