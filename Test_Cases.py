import unittest
import time
from Yahoo_Page import *
from Tools import *

class HomePageSetup(unittest.TestCase):

    #THIS HAS CHANGED  Please show this      

    #I initially had random password method here, moved it closer to where it is used
        
    def setUp(self):

        self.driver = webdriver.Chrome(options=options)  
        self.yahoo_page = Yahoo_Page(self.driver)      

    def tearDown(self):
        self.driver.quit()

class Search(HomePageSetup):
    """
    Confirm the cursor is present in the Search field after the yahoo home page is opened.
    After an arbitrary input is given to the search field confirm that clicking the search icon navigates
    the user to the search page.

    acceptance criteria   
    --------------------
    -The cursur is in the search field after the yahoo home page is opened.
    -When the search field is given an input, the user is navigated to the search page.
    """
    def test_cursur_on_search_field(self):
        
        #I know I need an action here due to the definition of what a test is. However the test relies on nothing happening; or the cursor being where it 'should' be after yahoo home page open's
        #time.sleep(1)
        self.assertEqual(self.yahoo_page.current_cursor_id(), self.yahoo_page.search_field_id())

    def test_search_page(self):
        
        self.yahoo_page.input_search_field('Kendrick Lamar')
        self.yahoo_page.click_search_button()
        self.assertIn('search', self.driver.current_url,
            '\nSearch: ' + self.yahoo_page.search_field_contents())  #recommended to do this for all asserts?

class Dynamic_Drop_Down(HomePageSetup):
    """
    For the Originals drop down menu within yahoo news;
    ensure this drop down's links sends the user to the correlating site.

    acceptance criteria   
    --------------------
    -When the link is clicked the user is sent to a different site.
    -The site's url or title has the same or a similar title to that of the text on the drop down link.
    """
    def convert_option_title_to_url_block(self,drop_down_option_title):
        excluded_word1 = 'the'
        replace_space= '-'
        return Tools().del_words_replace_space_of_string(drop_down_option_title,replace_space, excluded_word1)

    def setUp(self):
        super().setUp()
        self.yahoo_page.click_news_link()
        self.driver.maximize_window()       #needed to show drop down tab
        self.yahoo_page.hover_originals_drop_down()

    def test_any_random_tab(self):
        
        yahoo_page = self.yahoo_page
        yahoo_page.click_random_option_from_originals_drop_down()
        self.assertNotEqual(self.driver.title,'Yahoo News - Latest News & Headlines')
        self.assertIn(self.convert_option_title_to_url_block(yahoo_page._random_option_title()),self.driver.current_url)

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
        self.assertEqual(yahoo_page.password_error_message().text,"Your password is too easy to guess.")


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

        self.assertEqual(yahoo_page.password_error_message().get_attribute('data-error' or None),"")   #is it ok to put logic operators in here like this?
        self.assertEqual(yahoo_page.password_error_message().text,"")

if __name__ == "__main__": unittest.main()