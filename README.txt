To Run
Navigate to the root directory of the repository and run "python yahoo_test_suite.py". This works automatically on Windows 10 with ChromeDriver 85, adblocker and using Python 3.8. Given you have a PATH to bothe the driver and the extension

To facilitate running this on another OS, I included a Settings.py file and a Resources directory. In Resources you will find an adblocker directory with a folder called 3.9_0 (the version of the extension). If you cloned my repo then you only need to copy the path of the contents of the 3.9_0 folder and paste this into the adblocker_path variable within the Settings.py file. Also, in resources you will find different webDrivers. Choose your webDriver and follow the same process of copying the path, but this time with the chromedriver.exe executable included at the end of the path, then paste this into the Settings.py file variable. 

Note: I successfully ran the suite using a Mac, however if you receive a wrong permissions error you may need to download the mac ChromeDriver from https://chromedriver.chromium.org/ . I did not attempt running the test suite on Linux, but I plan too. 

To run the test cases Password_Link and Error_Message_Passwords you will need to create a yahoo account and copy your username and password into the variables provided in the Settings.py file. 


Notes
•	The Password_Link and Error_Message_Passwords test Cases can error due to the Yahoo site’s security checks. At times, the site will ask to prove you are not a robot or will say it noticed strange behavior on the account, which creates a time out error. The first time the tests are ran this rarely happens, this security check increases in frequency the more the site is logged into. In short it should run without erroring the first time the suite is ran. This is also noted in the docstring. 

•	For the Error_Message_Passwords test case I have a short password and long password that are far apart in lengths. I realize in production the lengths would likely be closer together and the criteria for a test like this would be provided in which I would need to meet this criteria. 

•	I avoided using time.sleep(), but because of the challenges of handling a pop up and the unavailability of development resources I used one time.sleep() in Yahoo_Page.py line 95. I understand that this is not optimal.

•	In yahoo_page.py line 57 I use a wait for invisibility on a locator. The XPATHs for those locators in 'moderate_password_error_message' are not great concerning its longengevity in production. Another solution for that invisibility wait is in the my_explicit_wait_ErrorMessagePasswords branch in this repository. In this branch I created my own Expected Condition that successfully waits for a dynamic element to not be itcd s previous attribute value. This Expected Condition is also in this branch in tools.py under unused tools.

A personal note
I hope you like this code, I enjoy constructive criticism so feel free to provide any. I have comments that give clarification on why some of my code is necessary. If any code needs further explanation, please let me know. I enjoyed this project and I hope to meet with you in person.
