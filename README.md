# Website_Automation_python

This project illustrates some fundamentals of website automation testing; it is written in python and uses selenium. 
I chose Yahoo.com because it possesses typical challenges in testing such as anti-bot security, dynamic drop downs, pop ups, and cookies.

This repository is PEP8 compliant, exhibits code modularity, its structure adheres to the Page Object Model, and each test is isolated.

The Repository https://github.com/agrant23/CsharpFrameWork exhibits improved code modularity, it adheres more to the POM

I tested this on Mac and Window Operating Systems. 
I created an Amazon EC2 instance in the AWS cloud environment. I connected to this instance via ssh using Linux. 
In this cloud environment I set up a python virtual environment where I pulled in my QA repository from Github and successfully ran and passed my test suite.
This was a great into into working with the Linux environment.


## To Run
1.  You need to create a yahoo account and copy your username and password into the variables provided in the settings.py file.
    You may need to login, logout and login again, manually to avoid anti-bot security. Also can manually navigate through yahoo security during navigation.
        If you want to.
        You can utilize the .gitignore file and create the "secure.py" file In this Repository, and fill in the code below: 
            yahoo_username = 'Your User Name@yahoo.com'
            yahoo_password = 'Your Password'

2.  Create a directory called "Website_Automation_python". 
    You need to set up your own Python equiped IDE or text editor.
        You can create a python virtual environment if convenient by using the command:s

            For Windows:
            python -m venv project_name.py
            pip install selenium

            For macOS/Linux:
            $ python -m venv myfirstproject
            $ pip install selenium

3.  With Git Bash navigate to the above directory and run:
        git clone git@github.com:agrant23/Website_Automation_python.git

4.  With an OS command prompt navigate to this same directory and run:
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
