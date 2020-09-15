#Yahoo_Page_3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from flask import Flask, make_response
import Secure 
import time
import string
from Tools import *

''' app = Flask(__name__)

@app.route('/')
def fix_cookies():
    response = make_response('Cookie should be disabled')
    response.set_cookie('cookie1', 'value1', samesite='None', secure=True)
    return response  '''

path_to_extension = r'C:\Webdrivers.Extensions\3.9_0'

options = Options()
options.add_argument('load-extension=' + path_to_extension)
#options.add_argument(fix_cookies())
#options.add_argument('--hide-scrollbars')
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('disable-gpu')        #GPU graphical processing unit
options.add_argument('window-size=1920x1080')  #fixes the hover__over_originals_drop_down 
options.add_argument('--log-level=3')
#options.set_headless
#options.add_argument('load-extension=' + path_to_extension) #the extension is adBlocker, this allows navigation without adds hiding
#options.set_headless(headless=True)

class Yahoo_Page():


    def __init__(self,driver):
        self.driver = driver
        driver.get("https://www.yahoo.com")

        #after loading adBlock extension it opens in a new window, I change AdBlock preferences then switch back to the yahoo window
        #self.change_adBlock_preferences()
        self.switch_to_tab()          

    #def load_website(self,home_url):     self.driver.get(home_url)  

    #def change_adBlock_preferences(self):
    #    AdBlock_tool_icon = self.driver.find_elements_by_xpath('//html[data_platform="chromium"]')

    def switch_to_tab(self):     
        #wait(self.driver, 15).until(EC.number_of_windows_to_be(2)) #in headless mode this is not seen, don't need this wait in headless or non-headless mode
        yahoo_window = self.driver.window_handles[0]    #for some reason self.driver.window_handles[-1] does not work
        self.driver.switch_to.window(yahoo_window)

    #Buttons

    def click_sign_in_button(self):
        sign_in_button_loc = (By.LINK_TEXT,'Sign in')                                             #'//a[@id="header-signin-link"]//span')       #added /span
        wait(self.driver,15).until(EC.element_to_be_clickable(sign_in_button_loc))
        self.driver.find_element(*sign_in_button_loc).click()
    
    def click_username_next_button(self):      
        username_next_button_loc = (By.ID,"login-signin") 
        wait(self.driver, 15).until(EC.element_to_be_clickable(username_next_button_loc))
        self.driver.find_element(*username_next_button_loc).click()
        
    def click_password_next_button(self):  self.driver.find_element_by_class_name("button-container").find_element_by_id('login-signin').click()
    
    def click_search_button(self):  
        search_button_loc = (By.XPATH,'//input[@type="submit"]')
        wait(self.driver, 15).until(EC.element_to_be_clickable(search_button_loc))
        self.driver.find_element(*search_button_loc).click()
        wait(self.driver,15).until_not(EC.title_is('Yahoo'))     #helpful wait for the next page to load

    #Fields

    def username_field(self):
        username_field_loc = (By.ID,'login-username')               
        wait(self.driver, 15).until(EC.presence_of_element_located(username_field_loc))
        return self.driver.find_element(*username_field_loc)      
    def input_username_field(self,userName):     self.username_field().send_keys(userName)

    def password_field(self):
        password_field_loc = (By.XPATH,"//input[@name='password']")        # "//input[@name='password']")
        wait(self.driver,15).until(EC.visibility_of_element_located(password_field_loc))       #presence_of_....
        return self.driver.find_element(*password_field_loc)       
    def input_password_field(self,passWord):
        self.password_field().send_keys(passWord)

    def new_password_field(self):
        new_password_field_loc = (By.XPATH,"//input[@name='password']")
        wait(self.driver,15).until(EC.presence_of_element_located(new_password_field_loc))
        return self.driver.find_element(*new_password_field_loc)    
    def input_new_password_field(self,newPassWord):   self.new_password_field().send_keys(newPassWord)

    def current_cursor_id(self):
        return self.driver.switch_to.active_element.get_attribute('id')
    
    def search_field(self):
        search_field_loc = (By.XPATH,"//form/input[@type='text']")  #or //form[@role='search']/input[@type='text']
        #wait(self.driver,15).until(EC.visibility_of_element_located(search_field_loc))
        wait(self.driver,15).until(EC.presence_of_element_located(search_field_loc))
        return self.driver.find_element(*search_field_loc)        
    def search_field_id(self):      return self.search_field().get_attribute('id')
    def input_search_field(self,search):    self.search_field().send_keys(search)
    def search_field_contents(self):    
        return self.driver.find_element_by_xpath('//input[@type="text"]').get_attribute('value')


    #Popups

    def pop_up_apperears_tab_off_it(self):
        wait(self.driver, 10).until(EC.url_changes('yahoo.com'))
        current_tab = self.driver.current_window_handle                  
        time.sleep(2)    #this is needed to give the pop up time to load/appear, no explicit wait handles this
        self.driver.switch_to.window(current_tab)        

    #Drop Downs

    def hover_over_profile_menu(self):
        profile_menu_loc = (By.XPATH,'//label[@role="presentation"]')
        wait(self.driver,15).until(EC.visibility_of_element_located(profile_menu_loc))
        #wait(self.driver,15).until(EC.element_to_be_clickable(profile_menu_loc))
        profile_menu_element = self.driver.find_element(*profile_menu_loc)                     #label[contains(@for,"AccountMenu")]/span').click()   # this xpath or this?  //input[contains(@id,"AccountMenu")]/following-sibling::label
        ActionChains(self.driver).move_to_element(profile_menu_element).perform()

    def click_profile_menu_settings(self):
        setting_link_loc = (By.LINK_TEXT,'Settings')
        wait(self.driver,15).until(EC.element_to_be_clickable(setting_link_loc))
        self.driver.find_element(*setting_link_loc).click()
    
    def hover_over_originals_drop_down(self):
        originals_drop_down_loc = (By.XPATH,'//a[@title="Originals"]')
        wait(self.driver,15).until(EC.visibility_of_element_located(originals_drop_down_loc))
        drop_down_element = self.driver.find_element(*originals_drop_down_loc)
        ActionChains(self.driver).move_to_element(drop_down_element).perform()

    #Tabs and Options

    def click_account_security_tab(self):       
        account_security_loc = (By.PARTIAL_LINK_TEXT,'Account Security')
        wait(self.driver,15).until(EC.presence_of_element_located(account_security_loc))
        self.driver.find_element(*account_security_loc).click()
    
    def click_The_Ideas_Election_option(self):
        The_IdeasElection_tab_loc = (By.XPATH,'//a[@title="The Ideas Election"]')
        wait(self.driver,15).until(EC.element_to_be_clickable(The_IdeasElection_tab_loc)) 
        self.driver.find_element(*The_IdeasElection_tab_loc).click()

    def click_random_option_from_originals_drop_down(self):
        all_options_loc = (By.XPATH,'//a[@title="Originals"]/following-sibling::div//a') #//a[contains(@class,"nr-subnav-link")]')
        wait(self.driver,15).until(EC.visibility_of_all_elements_located(all_options_loc))
        all_options = self.driver.find_elements(*all_options_loc)
        #all_options = self.driver.find_elements_by_xpath ('//a[contains(@class,"nr-subnav-link")]') #this does seem redundant
        #options that vary their internal links and are therefore not included in selecting a random option are, index # = Title: 2 = Baby Brain, 5 =2020 Vision Column, 6 = 2020 Candidate Tracker, 7 = The Ideas Election, 8 = Presidential Leadership Series.
        #random_option = all_options[6]
        random_option = all_options[Tools().generate_randon_number_with_excluded_nums(9,2,6)]
        self._random_option_title = random_option.get_attribute('title')
        _before_click_url = self.driver.current_url
        random_option.click()
        wait(self.driver,15).until(EC.url_changes(_before_click_url))
    
    def _random_option_title(self):
        return str.lower(self._rand_option_title)

    #Links

    def click_change_password_link(self):
        change_password_loc = (By.PARTIAL_LINK_TEXT,'Change password')
        wait(self.driver,15).until(EC.element_to_be_clickable(change_password_loc))
        self.driver.find_element(*change_password_loc).click()

    def click_news_link(self):        self.driver.find_element_by_link_text('News').click()

    #Action Keys

    def tab_to_next_field(self):  ActionChains(self.driver).send_keys(Keys.TAB).perform() 

    #User Flow

    def login(self):
        self.click_sign_in_button()
        self.input_username_field(Secure.yahoo_username) 
        self.click_username_next_button()
        self.input_password_field(Secure.yahoo_password)
        self.click_password_next_button()
        self.pop_up_apperears_tab_off_it() 

    def navigate_to_security_tab(self):
        self.hover_over_profile_menu()
        self.click_profile_menu_settings()
        self.click_account_security_tab()

    #Error Messages

    def password_error_message(self):
        password_status_loc = (By.ID,'cpwd-error-password')
        password_status_element = wait(self.driver,15).until(EC.presence_of_element_located(password_status_loc)) 
        return password_status_element

    #Exception Handling

    def time_out(self):       
        try:
            originals_drop_down_loc = (By.XPATH,'//a[@title="Originals"]')
            wait(self.driver,15).until(EC.visibility_of_element_located(originals_drop_down_loc))
        except TimeoutError as exception:
           raise exception


    #Get attributes

    #def drop_down_title(self): 