# Website_Automation_python

This project illustrates some fundamentals of website automation testing; it is written in python and uses selenium. I chose Yahoo.com because it possesses typical challenges in testing due to its anti-bot security, drop down, pop up, and cookie features. Dynamic elements are tested; a dynamic drop down, a search bar, and internal links are also tested. This repository is PEP8 compliant, exhibits modularity, its structure adheres to the Page Object Model, and though I use class inheritance in test cases the tests are isolated.

This repository will run on Windows, Mac, and Linux operating systems. To ensure this I tested it on a Mac OS, and I tested it on an ec2 Linux instance through Amazon Web Services (AWS). I created, connected to, and worked in the ec2 Linux server environment; this greatly furthered my experience in Linux and working with these microsystems.

## To Run
•	You need to create a yahoo account and copy your username and password into the variables provided in the settings.py file. 

•	Clone my repository:     
git clone git@github.com:agrant23/Website_Automation_python.git

•	Navigate to the root directory of the repository and run "python yahoo_test_suite.py". This works automatically on Windows, Linux, and Mac OSs using Python 3.9, and Selenium 3.141.

## Notes
•	The Password_Link and Error_Message_Passwords test Cases can error after multiple runs due to the anti-bot security checks. 

In yahoo_page.py line 57 I use an invisibility explicit wait. 

•	For the moderate and long password error message tests there is a dynamic element that required an explicit wait, I have two solutions for this element that you can compare, between the branches of my_explicit_wait_ErrorMessagePasswords (yahoo_page line 55, 72, and 75) and the master branch (yahoo_page line 57, 71. and 73). In the master branch I used multiple XPATHs for multiple locators to handle this element, the downside of this is using more XPATHs can lower a code's longengevity during production. In the other branch, I created my own Expected Condition that successfully waits for the dynamic element to not be its previous attribute value. The readability of this code is more challenging than the code in master branch. I feel it is debatable as to which branch gives the best solution for this dynamic element. Both branches have the Explicit Wait I created in tools.py.

•	I avoided using time.sleep(), but because of the challenges of handling a pop up and the unavailability of development resources I used one time.sleep() in yahoo_page.py line 169. I understand that this is not optimal.

•	I intentionally left many branches in this repository to show you its evolutionn over time and to illustrate my experiences using git. I would have renamed these branches to be more descriptive, but I found doing this can alter or lose my code in git.

## A personal note 
I hope you like this code, I enjoy constructive criticism so feel free to provide any. I provide clarifying comments throughout the repository. If any code needs further explanation, please let me know. I enjoyed this project and I hope to meet with you in person.
