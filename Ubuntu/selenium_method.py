import os,time, fuzzer_method
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def ByIdClicking(driver, id_name):
    element = driver.find_element_by_id(id_name)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.1)

def ByIdSendKey(driver, id_name, strings):
    driver.find_element_by_id(id_name).send_keys(strings)
    time.sleep(0.1)

class InitDriver(object):
    def SetChrome(self):
        driver = webdriver.Chrome('./chromedriver')
        return driver

class AddToContents(object):
    def Commit(self, driver):
        ByIdClicking(driver, 'top-nav-sub-file-dropdown__BV_toggle_')
        ByIdClicking(driver, 'top-nav-sub-file-dropdown-commit')
        ByIdClicking(driver, 'commitModalCommit')

    def ConfigureClear(self, driver):
        ByIdClicking(driver, 'top-nav-sub-edit-dropdown__BV_toggle_')
        ByIdClicking(driver, 'top-nav-sub-edit-dropdown-clear-configuration')

    def AddDevice(self, driver):
        # add device type
        ByIdClicking(driver, 'nav-left-search-add')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown__BV_toggle_')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown_option_Device')

        #add device group
        ByIdClicking(driver, 'newEntityModal_Group_dropdown__BV_toggle_')

        #create new group
        ByIdClicking(driver, 'newEntityModal_Group_dropdown_option_create_new_group')
    
    def AddServer(self, driver):
        element = driver.find_element_by_class_name('nav-left-search-add')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        ByIdClicking(driver, 'newEntityModal_Type_dropdown__BV_toggle_')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown_option_Server')

        ret = fuzzer_method.fuzz(23)
        ByIdSendKey(driver, 'newEntityModal_deviceName_input', ret)
        ByIdClicking(driver, 'newEntityModal_confirm_button')

    def TypeString(self, driver, ret):
        #input groupname and device name
        ByIdSendKey(driver, 'newEntityModal_groupName_input', ret)
        ByIdSendKey(driver, 'newEntityModal_deviceName_input', ret)


    def Confirm(self, driver):
        # click the Confirm button
        ByIdClicking(driver, 'newEntityModal_confirm_button')

    def AddDeviceOfDevice(self, driver, dv):
        element = driver.find_element_by_class_name('nav-left-search-add')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        ByIdClicking(driver, 'newEntityModal_Type_dropdown__BV_toggle_')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown_option_Device')
        ByIdClicking(driver, 'newEntityModal_Group_dropdown__BV_toggle_')

        id_name = 'newEntityModal_Group_dropdown_option_'+str(dv)
        # print(id_name)
        ByIdClicking(driver, id_name)

        ret2 = fuzzer_method.fuzz(5)
        ByIdSendKey(driver, 'newEntityModal_deviceName_input', ret2)

        print("ret2 ",ret2)

        return ret2

    def AddDeviceDetail(self, driver, gret, ret):
        name = 'lineDevice_device_'+str(gret)+'_'+str(ret)
        print(name)
        # element = driver.find_element_by_id(name)
        element = driver.find_element(By.XPATH, '//*[@id="lineDevice_device_' + str(gret) + '_' +str(ret) + '"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # manufacturer
        ret = fuzzer_method.fuzz()
        ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # Device type
        ret = fuzzer_method.fuzz()
        ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(1000)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_modbus_tcp_master')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # UID
        ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uid', '1')

        # Done
        ByIdClicking(driver, 'deviceConnectionButtonDone')

    def AddDeviceTag(self, driver, ret):
        # + click
        ByIdClicking(driver, 'datamapperAdd')

        # Tag id
        ByIdSendKey(driver, 'datamapperId_0', ret)
        # Start address
        ByIdSendKey(driver, 'datamapperInfo_address', str(40000+int(ret)))
        # length
        ByIdSendKey(driver, 'datamapperInfo_length', '1')        
        # value type
        ByIdClicking(driver, 'datamapperInfo_valueType__BV_toggle_')
        # select valutype
        ByIdClicking(driver, 'datamapperInfo_valueType_int')
        # interval
        ByIdSendKey(driver, 'datamapperInterval', '1000')

        # click done
        ByIdClicking(driver, 'datamapperAddDone')
    
    def AddServerDetail(self, driver):
        # edit button
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # manufacturer
        ret = fuzzer_method.fuzz()
        ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # Device type
        ret = fuzzer_method.fuzz()
        ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(1000)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)
        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')

        # Server detail input
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_modbus_tcp_slave')
        ByIdClicking(driver, 'deviceServiceButtonDone')

    def AddServerTag(self, driver, IDnum, dv):
        # add the detail
        ByIdClicking(driver, 'datamapperAdd')
        # Id
        ByIdSendKey(driver, 'datamapperId_0', IDnum)
        # Type
        ByIdClicking(driver, 'datamapperId_1__BV_toggle_')
        ByIdClicking(driver, 'datamapperId_1_holding')
        # Addr
        ByIdSendKey(driver, 'datamapperId_2', IDnum)
        # Category
        ByIdClicking(driver, 'datamapperInfo_category__BV_toggle_')
        # device
        ByIdClicking(driver, 'datamapperInfo_category_device')
        # Group
        ByIdClicking(driver, 'datamapperInfo_group__BV_toggle_')

        id_name = 'datamapperInfo_group_' + str(dv)
        ByIdClicking(driver, id_name)

        # Device
        ByIdClicking(driver, 'datamapperInfo_device__BV_toggle_')

        id_name = 'datamapperInfo_device_' + str(dv)
        ByIdClicking(driver, id_name)
        
        # Tag
        ByIdClicking(driver, 'datamapperInfo_tag__BV_toggle_')
        ByIdClicking(driver, 'datamapperInfo_tag_0')
        # Value Type
        ByIdClicking(driver, 'datamapperInfo_valueType__BV_toggle_')
        ByIdClicking(driver, 'datamapperInfo_valueType_int')
        # Done
        ByIdClicking(driver, 'datamapperAddDone')