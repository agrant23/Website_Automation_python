#Test_Password_Count_2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import random
import string
import time

class Test_Password_Count(unittest.TestCase):                  

    def setUp(self):
        path_to_extension = r'C:\Webdrivers.Extensions\3.9_0'
        options = Options() 
        options.add_argument('load-extension=' + path_to_extension)

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.yahoo.com")
        
        wait = WebDriverWait(self.driver, 10) 
        
        yahoo_tab = self.driver.current_window_handle
        wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(yahoo_tab)

        sign_in_button = self.driver.find_element_by_id("header-signin-link")
        sign_in_button.click()
        
        username_field_loc = (By.ID,'login-username')
        username_field = wait.until(                
            EC.presence_of_element_located(username_field_loc))
        username_field = self.driver.find_element(*username_field_loc)

        username_field.send_keys("tonyg1239411@yahoo.com") 

        next_button_loc = (By.XPATH,'//input[@id="login-signin"]')
        next_button1 = self.driver.find_element(*next_button_loc)
        next_button1 = wait.until(                  #can't replace WebDriverWait(self.driver,5) with wait 
            EC.element_to_be_clickable(next_button_loc))
        next_button1.click()

        password_field_loc = (By.XPATH,'//input[@id="login-passwd"]')
        password_field = wait.until(
            EC.presence_of_element_located(password_field_loc))
        password_field = self.driver.find_element(*password_field_loc)
       
        password_field.send_keys("Holler45#")
        
        next_button2 = self.driver.find_element_by_xpath('//button[@id="login-signin"]')
        next_button2.click()

        current_tab = self.driver.current_window_handle                  
        time.sleep(3)    #this is needed to give the pop up time to load/appear
        self.driver.switch_to.window(current_tab)
        
        profile_menu = self.driver.find_element_by_id('header-profile-menu')
        profile_menu.click() 
        
        setting_link_loc = (By.ID,'profile-settings-link')
        setting_link = self.driver.find_element(*setting_link_loc)
        setting_link = wait.until(
        EC.element_to_be_clickable(setting_link_loc))
        setting_link.click()

        account_security_loc = (By.PARTIAL_LINK_TEXT,'Account Security')
        account_security = self.driver.find_element(*account_security_loc)
        account_security = wait.until(
        EC.element_to_be_clickable(account_security_loc))
        account_security.click()

        change_password_loc = (By.PARTIAL_LINK_TEXT,'Change password')
        change_password = self.driver.find_element(*change_password_loc)
        change_password = wait.until(
        EC.element_to_be_clickable(change_password_loc))
        change_password.click()

    def test_password_character_min(self):                           
        actions = ActionChains(self.driver)
        action_tab = actions.send_keys(Keys.TAB)
        wait = WebDriverWait(self.driver, 10)

        chars_not_in_password = ['\n','\t','\r','\x0b','\x0c']
        for char in chars_not_in_password:
            password_characters = string.printable.replace(char,'')
                
        password_char_1 = ''
        password_char_2 = ''
        password_char_3 = ''
        password_char_4 = ''
        password_char_5 = ''
        password_char_6 = ''
        password_char_7 = ''

        password_char_1 = random.choice(password_characters)

        new_password_field = self.driver.find_element_by_id('cpwd-password')
        new_password_field.send_keys(password_char_1)  

        action_tab.perform()    #this is needed to see the correct/current password status message
        new_password_field.click()

        password_status_loc = (By.ID,'cpwd-error-password')
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc) #is this line needed here and through char_7

        self.assertEqual(password_status_element.text,"Your password is too easy to guess, try making it longer.")

        password_char_2 = random.choice(password_characters)
        new_password_field.send_keys(password_char_2)
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc) 

        self.assertEqual(password_status_element.text,"Your password is too easy to guess, try making it longer.")

        password_char_3 = random.choice(password_characters)
        new_password_field.send_keys(password_char_3)
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc)  

        self.assertEqual(password_status_element.text,"Your password is too easy to guess, try making it longer.")

        password_char_4 = random.choice(password_characters)
        new_password_field.send_keys(password_char_4)
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc)  

        password_char_5 = random.choice(password_characters)
        new_password_field.send_keys(password_char_5)
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc)  

        self.assertEqual(password_status_element.text,"Your password is too easy to guess, try making it longer.")

        password_char_6 = random.choice(password_characters)
        new_password_field.send_keys(password_char_6)
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc)  

        self.assertEqual(password_status_element.text,"Your password is too easy to guess, try making it longer.")

        password_char_7 = random.choice(password_characters)
        new_password_field.send_keys(password_char_7)
        password_status_element = wait.until(
            EC.presence_of_element_located(password_status_loc))
        password_status_element = self.driver.find_element(*password_status_loc)  

        self.assertEqual(password_status_element.text,"")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":                      
    unittest.main()  
