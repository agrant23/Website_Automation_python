#Yahoo_Page_3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import Secure 
import time
import string
from Tools import *

path_to_extension = r'C:\Webdrivers.Extensions\3.9_0'

options = Options()
options.add_argument('load-extension=' + path_to_extension) #the extension is adBlocker, this allows navigation without adds hiding


class Yahoo_Page():


    def __init__(self,driver):
        self.driver = driver
        driver.get("https://www.yahoo.com")

        #after loading an extension it opens a new tab, so I tab back to yahoo tab
        self.switch_to_tab()          

    def load_website(self,home_url):     self.driver.get(home_url)  

    #after loading an extension it opens a new tab, so I tab back to yahoo tab
    def switch_to_tab(self):     
        current_tab = self.driver.current_window_handle
        wait(self.driver, 15).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(current_tab)

    #Buttons

    def click_sign_in_button(self):
        sign_in_button_loc = (By.XPATH,'//a[@id="header-signin-link"]//span')       #added /span
        wait(self.driver,15).until(EC.element_to_be_clickable(sign_in_button_loc))
        self.driver.find_element(*sign_in_button_loc).click()
    
    def click_username_next_button(self):      
        username_next_button_loc = (By.ID,"login-signin") 
        wait(self.driver, 15).until(EC.element_to_be_clickable(username_next_button_loc))
        self.driver.find_element(*username_next_button_loc).click()
        
    def click_password_next_button(self):  self.driver.find_element_by_class_name("button-container").find_element_by_id('login-signin').click()
    
    def click_search_button(self):  
        search_button_loc = (By.ID,'header-desktop-search-button')
        wait(self.driver, 15).until(EC.element_to_be_clickable(search_button_loc))
        self.driver.find_element_by_id('header-desktop-search-button').click()

    #Fields

    def username_field(self):
        username_field_loc = (By.ID,'login-username')               
        wait(self.driver, 15).until(EC.presence_of_element_located(username_field_loc))
        return self.driver.find_element(*username_field_loc)      
    def input_username_field(self,userName):     self.username_field().send_keys(userName)

    def password_field(self):
        password_field_loc = (By.ID,"login-passwd")
        wait(self.driver,15).until(EC.presence_of_element_located(password_field_loc))
        return self.driver.find_element(*password_field_loc)       
    def input_password_field(self,passWord):    self.password_field().send_keys(passWord)

    def new_password_field(self):
        new_password_field_loc = (By.ID,'cpwd-password')
        wait(self.driver,15).until(EC.presence_of_element_located(new_password_field_loc))
        return self.driver.find_element(*new_password_field_loc)    
    def input_new_password_field(self,newPassWord):   self.new_password_field().send_keys(newPassWord)

    def current_cursor_id(self):
        return self.driver.switch_to.active_element.get_attribute('id')
    
    def search_field(self):
        search_field_loc = (By.ID,"header-search-input")
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

    def click_profile_menu(self):  self.driver.find_element_by_id('header-profile-menu').click()

    def click_profile_menu_settings(self):
        setting_link_loc = (By.ID,'profile-settings-link')
        wait(self.driver,15).until(EC.element_to_be_clickable(setting_link_loc))
        self.driver.find_element(*setting_link_loc).click()
    
    def hover_originals_drop_down(self):
        originals_drop_down_loc = (By.XPATH,'//a[@title="Originals"]')
        #self.driver.refresh()
        wait(self.driver,15).until(EC.visibility_of_element_located(originals_drop_down_loc))
        drop_down_element = self.driver.find_element(*originals_drop_down_loc)
        ActionChains(self.driver).move_to_element(drop_down_element).perform()

    #Tabs

    def click_account_security_tab(self):       
        account_security_loc = (By.PARTIAL_LINK_TEXT,'Account Security')
        wait(self.driver,15).until(EC.presence_of_element_located(account_security_loc))
        self.driver.find_element(*account_security_loc).click()
    
    def click_The_Ideas_Election_tab(self):
        The_IdeasElection_tab_loc = (By.XPATH,'//a[@title="The Ideas Election"]')
        wait(self.driver,15).until(EC.element_to_be_clickable(The_IdeasElection_tab_loc)) 
        self.driver.find_element(*The_IdeasElection_tab_loc).click()
        #script = getElementByXpath("//a[@title='The Ideas Election']") 
        #self.driver.execute_script('script.click();)

    def click_random_tab_from_originals_drop_down(self):
        all_tabs = self.driver.find_elements_by_xpath ('//a[contains(@class,"nr-subnav-link")]')
        random_tab = all_tabs[Tools().generate_randon_number(9)]
        self._rand_tab_title = random_tab.get_attribute('title')
        random_tab.click()
        #all_tabs_originals_loc = (By.XPATH,'//a[contains(@class,"nr-subnav-link")]')
        #random_tab_loc = 
        #wait(self.driver,15).until(EC.element_to_be_clickable(random_tab_loc))
    
    def random_tab_title(self):
        return str.lower(self._rand_tab_title)

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
        self.click_profile_menu()
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
        
    #Waits for page

    def navigate_off_News_page(self):    wait(self.driver,15).until_not(EC.title_is('Yahoo News - Latest News & Headlines'))


    #Get attributes

    #def drop_down_title(self): 