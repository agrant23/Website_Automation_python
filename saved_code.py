#Saved code

from selenium import webdriver
import settings
from yahoo_page import *
options = YahooPage.option
#unused Chrome commands thinking it will help with headless

options.add_argument('--no-sandbox')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')   #needed very much so
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-pre-commit-inpu') #new
options.add_argument('--disable-crash-reporter')
#options.add_argument('--dump-dom')                 #this broke it, created a Resource warning
options.add_argument('--enable-crash-reporter')
#options.add_argument('--font-render-hinting')      #this broke it, created a Resource warning

#In test_cases.py setUp(self)
from selenium.webdriver.chrome.service import Service  # fix for Selenium 4
s = Service(settings.path_to_webdriver)  #selenium 4
driver = webdriver.Chrome(services=s, options=options)

#get and add user_agent
user_agent = driver.execute_script("return navigator.userAgent;")
print(user_agent)
options.add_argument(f'user-agent={user_agent}')

driver.get_screenshot_as_file("screenshot.png")
