# Website_Automation_python

This project illustrates some fundamentals of website automation testing; it is written in python. I chose Yahoo.com because it possesses typical challenges in testing due to its anti-bot security, drop downs, and pop ups features. Dynamic elements are tested in the Error Message Password tests; a dynamic drop down, a search bar, and internal links are also tested. This repository is PEP8 compliant, exhibits modularity, its structure adheres to the Page Object Model, and is atomic testing.


## To Run
Navigate to the root directory of the repository and run "python yahoo_test_suite.py". This works automatically on Windows 10 with ChromeDriver 89, and using Python 3.9.

To facilitate running this on other Operating Systems, I included a settings.py file and a Resources directory. In Resources you will find an adblocker directory and webDrivers for different OSs. If you are not on a windows OS then you need to change the path_to_webdriver in the settings.py file accordingly. 

Note: I successfully ran the suite using a Mac, however if you receive a wrong permissions error you may need to download the mac ChromeDriver from https://chromedriver.chromium.org/.

To run the test cases Password_Link and Error_Message_Passwords you will need to create a yahoo account and copy your username and password into the variables provided in the settings.py file. 


## Notes
•	The Password_Link and Error_Message_Passwords test Cases can error due to the Yahoo sites security checks. It should run without erroring the first time the suite is ran, however the more it is ran the more likely it will error. 

•	I avoided using time.sleep(), but because of the challenges of handling a pop up and the unavailability of development resources I used one time.sleep() in Yahoo_Page.py line 169. I understand that this is not optimal.

•	In yahoo_page.py line 57 I use a wait for invisibility on a locator. The XPATHs for those locators in 'moderate_password_error_message' are not great concerning its longengevity in production. Another solution for that invisibility wait is in the my_explicit_wait_ErrorMessagePasswords branch in this repository. In this branch I created my own Expected Condition that successfully waits for a dynamic element to not be itcd s previous attribute value. This Expected Condition is also in this branch in tools.py under unused tools.

A personal note 
* I hope you like this code, I enjoy constructive criticism so feel free to provide any. I provide clarifying comments through out the repository. If any code needs further explanation, please let me know. I enjoyed this project and I hope to meet with you in person.
