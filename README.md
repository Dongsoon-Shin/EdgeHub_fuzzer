# [EdgeHub] UI fuzzer

This is EdgeHub fuzzer for EdgeHub UI testing. I'll demonstrate how to execute the script file. If end the testing, let me know your result @Dongsoon Shin. 

# Install

### Virtualenv

First, to avoid the crush other modules, I recommend that make "virtualenv".

    $ pip install virtualenv
    $ virtualenv -p python3 .venv

If you execute the above code, you cannot see the .venv folder if you use a Linux or Mac. But, It exists as a hidden folder. Next, we type and run below code:

    $ source .venv/bin/activate

Now, we activated the virtualenv. If you succeed to activate the virtualenv, you can see the below shell shape. IIf you fail to activate the virtualenv, you cannot see the (.venv).

    (.venv)$

Then, we need auto-gen framework selenium, which usually used in web browser testing. Selenium is extenstion module in python. Therefore, If we use a some automatic framework, we have to install selenium.

    (.venv)$ pip install selenium pandas

Next, to use an Edgehub testing module, you should copy the "EdgeHub_testing_module" folder to the "lib" folder under the ".venv" folder.

    (.venv)$ cp -R Edgehub_testing_modul .venv/lib/site-packages/

Now, we can run python script. Execute the python script matched your OS.

### Chromedriver

This script run with Chromedriver. However, Chromedriver has been changing and it provides to each OS. Download link here:

[https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/](https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/)

Please, download ChromeDriver 80 version in current releases for fit to your OS.

# Running

I wrote the code that predefined function and pre-necessary module using selenium in selenium_module.py. If you want to use other web sites, you should modify some code in selenium_module.py. Due to the compatibility of the web site, I cannot write the general-purpose code now (In the future, I will make a general-purpose code).

    # simple running
    python Windows_test.py

During the script is started, we have to turn off the power-save function in system configuration (such as, power-save mode, auto turn-off monitor, etc.). This is important that turn-off the power-save mode and auto-turn-off the monitor (include screen savor). 

# Result

If the testing is end, you can see the log in console. Please, let me know your log.