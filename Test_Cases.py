import unittest
import time
from Yahoo_Page import *
from Tools import *


class HomePageSetup(unittest.TestCase):

    def setUp(self):
    
        self.driver = webdriver.Chrome(options=options)  
        self.yahoo_page = Yahoo_Page(self.driver)      

    def tearDown(self):
        self.driver.quit()


class Search(HomePageSetup):
    """
    Confirm the cursor is present in the Search field after the yahoo home page is opened.
    After an arbitrary input is given to the search field confirm that clicking the search button navigates
    the user to the search page.

    acceptance criteria   
    --------------------
    -The cursor is in the search field after the yahoo home page is opened.
    -When the search field is given an input, the user is navigated to the search page.
    """
    def test_cursur_on_search_field(self):
        
        self.assertEqual(self.yahoo_page.current_cursor_id(), self.yahoo_page.search_field_id())

    def test_search_page(self):
        
        self.yahoo_page.input_search_field('Kendrick Lamar')
        self.yahoo_page.click_search_button()
        self.assertIn('search', self.driver.current_url,
            '\nSearch of: ' + self.yahoo_page.search_field_contents() + "failed")


class Dynamic_Drop_Down(HomePageSetup):
    """
    For the Originals drop down menu within yahoo news;
    ensure that clicking on this drop down's options sends the user to the correlating site.

    acceptance criteria   
    --------------------
    -The title of the Originals drop down options is similar to that of the correlating site, given by the provided dictionary.
    """
    def convert_option_title_to_url_block(self,option_title):

                                    #Dictionary of option title as the key and the corresponding url block as the value.
        dict_option_title_url_block = {'The 360':'360' , 'Skullduggery':'skullduggery',
                                       'California Wildfires':'california-wildfires',
                                       'Conspiracyland':'conspiracyland' , '2020 Vision Column':'2020-vision',
                                       '2020 Candidate Tracker':'elections' , 'The Ideas Election':'the-ideas-election',
                                       'Presidential Leadership Series':'when-presidents-lead' ,
                                       'Through Her Eyes':'through-her-eyes'}
        
        return  Tools().dictionary_value_from_key(dict_option_title_url_block, option_title)

    def setUp(self):
        super().setUp()
        self.yahoo_page.click_news_link()
        self.driver.maximize_window()       #This is needed to be able to see and hover over the originals drop down tab.
        self.yahoo_page.hover_over_originals_drop_down()

    def test_any_random_tab(self):  
        yahoo_page = self.yahoo_page
        yahoo_page.click_random_option_from_originals_drop_down()
        self.assertIn(self.convert_option_title_to_url_block(yahoo_page.random_option_title),self.driver.current_url)


class Log_In_Link(HomePageSetup):

    def test_log_in_link(self):
        """ 
        Confirm the log in internal link is correct. 

        acceptance criteria   
        --------------------
        -After clicking the sign in button, the URL has changed to the login page. 
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
        Confirm the change password internal link is correct. 

        acceptance criteria   
        --------------------
        -After clicking the change password button, the URL has changed to the login page. 
        """

        self.yahoo_page.click_change_password_link()
        self.assertIn('change-password', self.driver.current_url)


class Error_Message_Passwords(HomePageSetup):

    def random_password(self, password_len): 
        excluded_password_chars = ['\n','\t','\r','\x0b','\x0c']                
        return Tools().generate_random_string(excluded_password_chars, password_len)

    def setUp(self):
        super().setUp()

        self.yahoo_page.login()
        self.yahoo_page.navigate_to_security_tab()
        self.yahoo_page.click_change_password_link() 

    def test_short_password_error_message(self):
        """ 
        Confirm that when the password is one character short of the minimum length required, the error data is present.
        Confirm the resulting error text is the same as before. 

        acceptance criteria   
        --------------------
        -When a password that is one character too short is entered,
        the data error does exist and the error text does appear.

        Note
        --------------------
        -Yahoo security will randomly ask to "prove you are not a robot". Which, at times, is responsible for this test erroring.  
        """     
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(5))
        yahoo_page.tab_to_next_field()   #tab to the Confirm Password field is needed to load the error message
        self.assertEqual(yahoo_page.password_error_message().get_attribute('data-error'),"WEAK_PASSWORD")  
        self.assertEqual(yahoo_page.password_error_message().text,"Your password is too easy to guess.")

    def test_long_password_error_message(self):
        """ 
        Confirm that when the password is one character longer than the maximum length allowed, the error data is not present.
        Confirm there is no error text after entering a password of sufficient length.

        acceptance criteria   
        --------------------
        -When a password that is one character too long is entered,
        the data error does not exist and the error text does not appears.

        Note
        --------------------
        -Yahoo security will randomly ask to "prove you are not a robot". Which, at times, is responsible for this test erroring.  
        """
        yahoo_page = self.yahoo_page

        yahoo_page.input_new_password_field(self.random_password(10))       
        yahoo_page.tab_to_next_field()      

        self.assertEqual(yahoo_page.password_error_message().get_attribute('data-error'),"")
        self.assertTrue(yahoo_page.password_error_message().text=="" or yahoo_page.password_error_message().text==None,
                        "\n" + yahoo_page.password_error_message().text + ' appeared instead of an empty string or None')

if __name__ == "__main__": unittest.main()