import os,time, fuzzer_method
from selenium import webdriver

class InitDriver(object):
    def SetChrome(self):
        driver = webdriver.Chrome('./chromedriver')
        return driver

class AddToContents(object):
    def ConfigureClear(self, driver):
        element = driver.find_element_by_id('top-nav-sub-edit-dropdown__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        element = driver.find_element_by_id('top-nav-sub-edit-dropdown-clear-configuration')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

    def AddDevice(self, driver):
        # add device type
        element = driver.find_element_by_class_name('nav-left-search-add')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        element = driver.find_element_by_id('newEntityModal_Type_dropdown__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        element = driver.find_element_by_id('newEntityModal_Type_dropdown_option_Device')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        #add device group
        element = driver.find_element_by_id('newEntityModal_Group_dropdown__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        #create new group
        element = driver.find_element_by_id('newEntityModal_Group_dropdown_option_create_new_group')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

    def TypeString(self, driver, ret):
        #input groupname and device name
        driver.find_element_by_id('newEntityModal_groupName_input').send_keys(ret)
        time.sleep(0.1)

        driver.find_element_by_id('newEntityModal_deviceName_input').send_keys(ret)
        time.sleep(0.1)

    def Confirm(self, driver):
        # click the Confirm button
        element = driver.find_element_by_id('newEntityModal_confirm_button')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

    def AddDeviceTag(self, driver, ret):
        element = driver.find_element_by_class_name('nav-left-search-add')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        element = driver.find_element_by_id('newEntityModal_Type_dropdown__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        element = driver.find_element_by_id('newEntityModal_Type_dropdown_option_Device')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        element = driver.find_element_by_id('newEntityModal_Group_dropdown__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        id_name = 'newEntityModal_Group_dropdown_option_'+str(ret)
        #print(id_name)
        element = driver.find_element_by_id(id_name)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        ret2 = fuzzer_method.fuzz(100,32,127)
        driver.find_element_by_id('newEntityModal_deviceName_input').send_keys(ret2)
        time.sleep(0.1)
