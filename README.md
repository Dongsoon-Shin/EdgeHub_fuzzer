# [EdgeHub] UI fuzzer

This is EdgeHub fuzzer for EdgeHub UI testing. I'll demonstrate how to execute the script file. If end the testing, let me know your result @Dongsoon Shin. 


# Install


First, to avoid the crush other modules, I recommend that make "virtualenv".

    pip install virtualenv
    virtualenv -p python3 .venv

If you execute the above code, you cannot see the .venv folder if you use a Linux or Mac. But, It exists as a hidden folder. Next, we type and run below code

    source .venv/bin/activate

Now, we activated the virtualenv. If you succeed to activate the virtualenv, you can see the below shell shape. IIf you fail to activate the virtualenv, you cannot see the (.venv).

    (.venv)$

Then, we need auto-gen framework selenium, which usually used in web browser testing. Selenium is extenstion module in python. Therefore, If we use a some automatic framework, we have to install selenium.

    (.venv)$ pip install selenium

Now, we ready for running the script.

# Running


I wrote the code that predefined function and pre-necessary module using selenium in selenium_module.py. If you want to use other web sites, you should modify some code in selenium_module.py. Due to the compatibility of the web site, I cannot write the general-purpose code now (In the future, I will make a general-purpose code).

    # simple running
    ./test.py

During the script is started, we have to turn off the save-power function in system configuration (such as, power-save mode, auto turn-off monitor, etc.). This is important that turn-off the power-save mode and auto-turn-off the monitor (include screen savor). 

# Result

If the testing is end, you can see the log in console. Please, let me know that log.
