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
options1 = Options()
options1.add_argument('load-extension=' + path_to_extension)

#change
#change 2


class Yahoo_Page_3():

    def __init__(self,driver):
        self.driver = driver

    def load_website(self,home_url,driver):     driver.get(home_url)     

    #after loading an extension it opens a new tab, so I tab back to yahoo tab
    def switch_to_tab(self,driver):     
        current_tab = driver.current_window_handle
        wait(driver, 15).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(current_tab)

    #Buttons

    def sign_in_button_click(self,driver):       driver.find_element_by_id("header-signin-link").click()
    
    def username_next_button(self,driver):      
        username_next_button_loc = (By.ID,"login-signin") 
        wait(driver, 15).until(EC.element_to_be_clickable(username_next_button_loc))
        return driver.find_element(*username_next_button_loc)
        
    def password_next_button(self,driver):  return driver.find_element_by_class_name("button-container").find_element_by_id('login-signin')

    def click(self,element):         element.click()
    
    #Fields

    def get_username_field(self,driver):
        username_field_loc = (By.ID,'login-username')               
        username_field = wait(driver, 15).until(EC.presence_of_element_located(username_field_loc))
        #username_field = driver.find_element(*username_field_loc)       #don't need this and one below since I'm not clicking it here?
        return username_field

    def get_password_field(self,driver):
        password_field_loc = (By.ID,"login-passwd")
        password_field = wait(driver,15).until(EC.presence_of_element_located(password_field_loc))
        #password_field = driver.find_element(*password_field_loc)
        return password_field

    def get_new_password_field(self,driver):
        new_password_field_loc = (By.ID,'cpwd-password')
        new_password_field_element = wait(driver,15).until(EC.presence_of_element_located(new_password_field_loc))
        return new_password_field_element

    #Inputs

    def input_string(self,my_string,element):     element.send_keys(my_string)   


    #Popups

    def tab_off_pop_up(self,driver):
        wait(driver, 10).until(EC.url_changes('yahoo.com'))
        current_tab = driver.current_window_handle                  
        time.sleep(2)    #this is needed to give the pop up time to load/appear, no explicit wait handles this
        driver.switch_to.window(current_tab)        

    #Drop Downs

    def profile_menu(self,driver):  return driver.find_element_by_id('header-profile-menu')

    def profile_menu_settings(self,driver):
        setting_link_loc = (By.ID,'profile-settings-link')
        setting_link = wait(driver,15).until(EC.element_to_be_clickable(setting_link_loc))
        setting_link = driver.find_element(*setting_link_loc)
        return setting_link
    
    #Tabs

    def account_security_tab(self,driver):       
        account_security_loc = (By.PARTIAL_LINK_TEXT,'Account Security')
        account_security = wait(driver,15).until(EC.presence_of_element_located(account_security_loc))
        return account_security
    
    #Links

    def change_password_link(self,driver):
        change_password_loc = (By.PARTIAL_LINK_TEXT,'Change password')
        change_password = wait(driver,15).until(EC.element_to_be_clickable(change_password_loc))
        return change_password

    #Action Keys

    def tab_to_next_field(self,driver):  ActionChains(driver).send_keys(Keys.TAB).perform() 

    #Error Messages

    def password_error_message(self,driver):
        password_status_loc = (By.ID,'cpwd-error-password')
        password_status_element = wait(driver,15).until(EC.presence_of_element_located(password_status_loc)) 
        return password_status_element