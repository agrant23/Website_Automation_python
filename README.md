# Website_Automation_python

This project illustrates some fundamentals of website automation testing; it is written in python and uses selenium. 
I chose Yahoo.com because it possesses typical challenges in testing such as anti-bot security, dynamic drop downs, pop ups, and cookies.

This repository is PEP8 compliant, exhibits code modularity, its structure adheres to the Page Object Model, and each test is isolated.

The Repository https://github.com/agrant23/CsharpFrameWork exhibits improved code modularity, it adheres more to the POM

I tested this on Mac and Window OSs. 
I created an ec2 Linux server environment (also called an Amazon Web Service Instance). I configured the AWS's security system manually, as it was free.
In this instance I created a python testing environment, there I remotely connected to my repository, pulled in this Repo and successfully tested the code.
    This testing environment required an IDE shell, with packages, the WebDriver, setting up multiple paths, and more. This was a great into into working with the Linux environment.

## To Run
•   You need to create a yahoo account and copy your username and password into the variables provided in the settings.py file.
    You may need to login, logout and login again, manually to avoid anti-bot security from being present for the testing of this repo.
        
        You can utilize the .gitignore file and create the "secure.py" file. In this file, fill in the code below: 
            yahoo_username = 'Your User Name@yahoo.com'
            yahoo_password = 'Your Password'

•   Create a directory called "Website_Automation_python". In this directory you need to set up your own Python enabled IDE or text editor.
        You can create a python virtual environment if convenient by using the command:
        
            For Windows:
            python -m venv project_name.py
            For macOS/Linux:
            $ python -m venv myfirstproject

•   With Git Bash navigate to the above directory and run:
        git clone git@github.com:agrant23/Website_Automation_python.git

•   With an OS command prompt navigate to this same directory and run:
        python yahoo_test_suite.py 

This works on Windows, Linux, and Mac OSs using Python 3.9, and Selenium 3.141.

## Notes
•   The Password_Link and Error_Message_Passwords test Cases can error after multiple runs due to the anti-bot security checks. 

•   In yahoo_page.py line 57 I use an invisibility explicit wait. 

•   I created my own Expected Condition that successfully waits for a dynamic element to not be its previous attribute value. Seen in Tools

•   I used one time.sleep() in yahoo_page.py line 169. I understand that this is not optimal.

•   I intentionally left many branches in this repository to show you its evolution over time; showing my experiences. 
    I would have renamed these branches to be more descriptive, but git has information integrity issues when attempting this.

## A personal note 
I hope you like this code, I enjoy constructive criticism so feel free to provide any. I provide clarifying comments throughout the repository which is open to comments as well.