import os,time, fuzzer_method
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    def AddDeviceOfDevice(self, driver, ret):
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

    def AddDeviceDetail(self, driver, ret):
        element = driver.find_element_by_id('lineDevice_device_Device_01_Device_01')
        #element = driver.find_element(By.XPATH, '//*[@id="lineDevice_device_Device_01"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        element = driver.find_element_by_id('deviceDetailButtonEdit')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        driver.find_element_by_id('deviceDetail_manufacturer').send_keys(ret)
        time.sleep(0.1)

        driver.find_element_by_id('deviceDetail_device_type').send_keys(ret)
        time.sleep(0.1)

        driver.find_element_by_id('deviceDetail_comment').send_keys(ret)
        time.sleep(0.1)

        element = driver.find_element_by_id('deviceDetailButtonDone')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        
        element = driver.find_element_by_id('deviceServiceButtonEdit')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        element = driver.find_element_by_id('deviceServiceSelect__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        element = driver.find_element_by_id('deviceServiceSelect_modbus_tcp_master')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        element = driver.find_element_by_id('deviceServiceButtonDone')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
    
    def AddDeviceTag(self, driver, ret):
        element = driver.find_element_by_id('datamapperAdd')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        # Tag id
        driver.find_element_by_id('datamapperId_0').send_keys(ret)
        time.sleep(0.1)

        # Start address
        driver.find_element_by_id('datamapperInfo_address').send_keys(str(40000+int(ret)))
        time.sleep(0.1)

        # length
        driver.find_element_by_id('datamapperInfo_length').send_keys("1")
        time.sleep(0.1)
        
        # value type
        element = driver.find_element_by_id('datamapperInfo_valueType__BV_toggle_')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        # select float
        element = driver.find_element_by_id('datamapperInfo_valueType_int')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)
        
        # interval
        driver.find_element_by_id('datamapperInterval').send_keys('1000')
        time.sleep(0.1)

        # click done
        element = driver.find_element_by_id('datamapperAddDone')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)




        

 