#Yahoo_Page_3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

path_to_extension = r'C:\Webdrivers.Extensions\3.9_0'
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> yahoo_test_ver4
options1 = Options()
options1.add_argument('load-extension=' + path_to_extension)


class Yahoo_Page_3():
<<<<<<< HEAD
=======
options = Options()
options.add_argument('load-extension=' + path_to_extension)


class Yahoo_Page():
>>>>>>> 4828c49719da17275be976331c5c4842ebba1872
=======
>>>>>>> yahoo_test_ver4

    def __init__(self,driver):
        self.driver = driver   

    def load_website(self,home_url):     self.driver.get(home_url)  

<<<<<<< HEAD
<<<<<<< HEAD
=======
    #Switching to Tabs and Websites

>>>>>>> 4828c49719da17275be976331c5c4842ebba1872
=======
>>>>>>> yahoo_test_ver4
    #after loading an extension it opens a new tab, so I tab back to yahoo tab
    def switch_to_tab(self):     
        current_tab = self.driver.current_window_handle
        wait(self.driver, 15).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(current_tab)

<<<<<<< HEAD
<<<<<<< HEAD
=======
    def open_login_page(self):
        wait(self.driver,15).until_not(EC.title_is('Yahoo'))

>>>>>>> 4828c49719da17275be976331c5c4842ebba1872
=======
>>>>>>> yahoo_test_ver4
    #Buttons

    def click_sign_in_button(self):
        sign_in_button_loc = (By.ID,"header-signin-link")
        wait(self.driver,15).until(EC.element_to_be_clickable(sign_in_button_loc))
        self.driver.find_element(*sign_in_button_loc).click()
    
    def click_username_next_button(self):      
        username_next_button_loc = (By.ID,"login-signin") 
        wait(self.driver, 15).until(EC.element_to_be_clickable(username_next_button_loc))
        self.driver.find_element(*username_next_button_loc).click()
        
    def click_password_next_button(self):  self.driver.find_element_by_class_name("button-container").find_element_by_id('login-signin').click()
    
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

    #Popups

    def tab_off_pop_up(self):
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
    
    #Tabs

    def click_account_security_tab(self):       
        account_security_loc = (By.PARTIAL_LINK_TEXT,'Account Security')
        wait(self.driver,15).until(EC.presence_of_element_located(account_security_loc))
        self.driver.find_element(*account_security_loc).click()
    
    #Links

    def click_change_password_link(self):
        change_password_loc = (By.PARTIAL_LINK_TEXT,'Change password')
        wait(self.driver,15).until(EC.element_to_be_clickable(change_password_loc))
        self.driver.find_element(*change_password_loc).click()

    #Action Keys

    def tab_to_next_field(self,):  ActionChains(self.driver).send_keys(Keys.TAB).perform() 
<<<<<<< HEAD
<<<<<<< HEAD

=======
    
>>>>>>> 4828c49719da17275be976331c5c4842ebba1872
=======

>>>>>>> yahoo_test_ver4
    #Error Messages

    def password_error_message(self):
        password_status_loc = (By.ID,'cpwd-error-password')
        password_status_element = wait(self.driver,15).until(EC.presence_of_element_located(password_status_loc)) 
        return password_status_element