import secure
import sys
import os


if sys.platform.startswith('win64'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       "/Resources/adblocker/3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/windows chromedriver/chromedriver.exe")
elif sys.platform.startswith('win32'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       "/Resources/adblocker/3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/windows chromedriver/chromedriver.exe")
elif sys.platform.startswith('linux'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       "/Resources/adblocker/3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/linux chromedriver/chromedriver")
elif sys.platform.startswith('darwin'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       "/Resources/adblocker/3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/windows chromedriver/chromedriver")


#replace secure.yahoo_username and secure.yahoo_password with the 
#username and password that you created.
yahoo_username = secure.yahoo_username
yahoo_password = secure.yahoo_password
