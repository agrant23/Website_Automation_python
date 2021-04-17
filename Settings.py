import secure
import sys
import os


# replace your yahoo user name and password with the variable values below

if sys.platform.startswith('win32'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       r"\Resources\adblocker\3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "\Resources\windows chromedriver\chromedriver.exe")
elif sys.platform.startswith('linux'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       r"/Resources/adblocker/3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/linux chromedriver/chromedriver")
elif sys.platform.startswith('darwin'):
    path_to_adBlock = (os.path.dirname(os.path.realpath(__file__)) + 
                       r"/Resources/adblocker/3.9_0")
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/windows chromedriver/chromedriver")

yahoo_username = secure.yahoo_username
yahoo_password = secure.yahoo_password
