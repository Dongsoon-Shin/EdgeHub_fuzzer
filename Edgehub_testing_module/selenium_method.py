import time, platform, os
from Edgehub_testing_module import fuzzer_method
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def ByIdClicking(driver, id_name):
    element = driver.find_element_by_id(id_name)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.1)

def ByClassClicking(driver, id_name):
    element = driver.find_element_by_class_name(id_name)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.1)

def ByIdSendKey(driver, id_name, strings):
    driver.find_element_by_id(id_name).send_keys(strings)
    time.sleep(0.1)

def ByXpathClicking(driver, id_name):
    element = driver.find_element(By.XPATH, id_name)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.1)

class InitDriver(object):
    def SetChrome(self):
        print(f"[!] System OS detected: {platform.system()}")
        if platform.system() != "Windows":
            driver = webdriver.Chrome('./chromedriver')
            return driver
        else:
            path = os.path.join("Windows", "chromedriver.exe")
            # print(file_name, path)
            driver = webdriver.Chrome(path)
            return driver

class AddToContents(object):
    def Commit(self, driver):
        ByIdClicking(driver, 'top-nav-sub-file-dropdown__BV_toggle_')
        ByIdClicking(driver, 'top-nav-sub-file-dropdown-commit')
        ByIdClicking(driver, 'commitModalCommit')

    def ConfigureClear(self, driver):
        ByIdClicking(driver, 'top-nav-sub-edit-dropdown__BV_toggle_')
        ByIdClicking(driver, 'top-nav-sub-edit-dropdown-clear-configuration')
        ByIdClicking(driver, 'commitModalCommit')

    def AddDevice(self, driver, ret):
        # add device type
        ByClassClicking(driver, 'nav-left-search-add')

        ByIdClicking(driver, 'newEntityModal_Type_dropdown__BV_toggle_')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown_option_Device')

        #add device group
        ByIdClicking(driver, 'newEntityModal_Group_dropdown__BV_toggle_')

        #create new group
        ByXpathClicking(driver,'//*[@id="newEntityModal_Group_dropdown"]/ul/li[1]/a')
        # ByIdClicking(driver, 'newEntityModal_Group_dropdown_option_create_new_group')

        #input groupname and device name
        ByIdSendKey(driver, 'newEntityModal_groupName_input', ret)
        ByIdSendKey(driver, 'newEntityModal_deviceName_input', ret)

         # click the Confirm button
        ByIdClicking(driver, 'newEntityModal_confirm_button')
    
    def AddServer(self, driver, ret):
        ByClassClicking(driver, 'nav-left-search-add')

        ByIdClicking(driver, 'newEntityModal_Type_dropdown__BV_toggle_')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown_option_Server')

        # ret = fuzzer_method.fuzz(20)
        ByIdSendKey(driver, 'newEntityModal_deviceName_input', ret)
        ByIdClicking(driver, 'newEntityModal_confirm_button')

    def AddDeviceOfDevice(self, driver, dv):
        ByClassClicking(driver,'nav-left-search-add')

        ByIdClicking(driver, 'newEntityModal_Type_dropdown__BV_toggle_')
        ByIdClicking(driver, 'newEntityModal_Type_dropdown_option_Device')
        ByIdClicking(driver, 'newEntityModal_Group_dropdown__BV_toggle_')

        # print(id_name)
        ByIdClicking(driver, f'newEntityModal_Group_dropdown_option_{str(dv)}')

        ret2 = fuzzer_method.fuzz(5)
        ByIdSendKey(driver, 'newEntityModal_deviceName_input', ret2)

        # print("ret2 ",ret2)

        return ret2

    def AddDeviceDetail_TCP(self, driver, gret, ret, UID, address, port, CC, TimeOut):
        # print(name)
        ByXpathClicking(driver, f'//*[@id="lineDevice_device_{str(gret)}_{str(ret)}"]')

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_modbus_tcp_master')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # Addr
        for i in range(15):
            ByIdSendKey(driver, 'deviceConnectionInput_address', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_address', address)

        # port
        ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_port', port)

        # Connection Count
        ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_connections', CC)

        # UID
        ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uid', UID)

        # Timeout
        ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_timeout', TimeOut)

        # Done
        ByIdClicking(driver, 'deviceConnectionButtonDone')

    def AddDeviceDetail_RTU(self, driver, gret, ret):
        # print(name)
        ByXpathClicking(driver, f'//*[@id="lineDevice_device_{str(gret)}_{str(ret)}"]')

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_modbus_rtu_master')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        # ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # Addr
        # for i in range(15):
        #     ByIdSendKey(driver, 'deviceConnectionInput_address', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_address', address)

        # port
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', port)

        # # Connection Count
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', CC)

        # # UID
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', UID)

        # # Timeout
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', TimeOut)

        # Done
        # ByIdClicking(driver, 'deviceConnectionButtonDone')

    def AddDeviceDetail_FENET(self, driver, gret, ret):
        # print(name)
        ByXpathClicking(driver, f'//*[@id="lineDevice_device_{str(gret)}_{str(ret)}"]')

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_fenet')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        # ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # # Addr
        # for i in range(15):
        #     ByIdSendKey(driver, 'deviceConnectionInput_address', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_address', address)

        # # port
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', port)

        # # Connection Count
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', CC)

        # # UID
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', UID)

        # # Timeout
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', TimeOut)

        # Done
        # ByIdClicking(driver, 'deviceConnectionButtonDone')

    def AddDeviceDetail_CNET(self, driver, gret, ret):
        # print(name)
        ByXpathClicking(driver, f'//*[@id="lineDevice_device_{str(gret)}_{str(ret)}"]')

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_cnet')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        # ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # # Addr
        # for i in range(15):
        #     ByIdSendKey(driver, 'deviceConnectionInput_address', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_address', address)

        # # port
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', port)

        # # Connection Count
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', CC)

        # # UID
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', UID)

        # # Timeout
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', TimeOut)

        # Done
        # ByIdClicking(driver, 'deviceConnectionButtonDone')

    def AddDeviceDetail_MELSEC_SERIAL(self, driver, gret, ret):
        # print(name)
        ByXpathClicking(driver, f'//*[@id="lineDevice_device_{str(gret)}_{str(ret)}"]')

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_melsec_serial')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        # ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # # Addr
        # for i in range(15):
        #     ByIdSendKey(driver, 'deviceConnectionInput_address', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_address', address)

        # # port
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', port)

        # # Connection Count
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', CC)

        # # UID
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', UID)

        # # Timeout
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', TimeOut)

        # Done
        # ByIdClicking(driver, 'deviceConnectionButtonDone')
    
    def AddDeviceDetail_MELSEC_ETHERNET(self, driver, gret, ret):
        # print(name)
        ByXpathClicking(driver, f'//*[@id="lineDevice_device_{str(gret)}_{str(ret)}"]')

        # Edit
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)

        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')
        
        # Device service
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_melsec_ethernet')
        ByIdClicking(driver, 'deviceServiceButtonDone')
        # ByIdClicking(driver, 'deviceConnectionButtonEdit')

        # # Addr
        # for i in range(15):
        #     ByIdSendKey(driver, 'deviceConnectionInput_address', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_address', address)

        # # port
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_port', port)

        # # Connection Count
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_connections', CC)

        # # UID
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_uid', UID)

        # # Timeout
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', Keys.BACKSPACE)
        # ByIdSendKey(driver, 'deviceConnectionInput_timeout', TimeOut)

    def AddDeviceTag(self, driver, tag, addr, length, valueType, interval):
        # + click
        ByIdClicking(driver, 'datamapperAdd')

        # Tag id
        ByIdSendKey(driver, 'datamapperId_0', tag)
        # Start address
        ByIdSendKey(driver, 'datamapperInfo_address', str(addr))
        # length
        ByIdSendKey(driver, 'datamapperInfo_length', str(length))
        # value type
        ByIdClicking(driver, 'datamapperInfo_valueType__BV_toggle_')
        # select valutype
        ByIdClicking(driver, f'datamapperInfo_valueType_{valueType}')
        # interval
        ByIdSendKey(driver, 'datamapperInterval', str(interval))

        # click done
        ByIdClicking(driver, 'datamapperAddDone')
    
    def AddServerDetail(self, driver, UIDs, Port):
        # edit button
        ByIdClicking(driver, 'deviceDetailButtonEdit')

        # manufacturer
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_manufacturer', ret)
        # # Device type
        # ret = fuzzer_method.fuzz()
        # ByIdSendKey(driver, 'deviceDetail_device_type', ret)
        # Comment
        ret = fuzzer_method.fuzz(100)
        ByIdSendKey(driver, 'deviceDetail_comment', ret)
        # Done
        ByIdClicking(driver, 'deviceDetailButtonDone')

        # Server detail input
        ByIdClicking(driver, 'deviceServiceButtonEdit')
        ByIdClicking(driver, 'deviceServiceSelect__BV_toggle_')
        ByIdClicking(driver, 'deviceServiceSelect_modbus_tcp_slave')
        ByIdClicking(driver, 'deviceServiceButtonDone')

        ByIdClicking(driver, 'deviceConnectionButtonEdit')

        ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_port', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_port', Port)

        ByIdSendKey(driver, 'deviceConnectionInput_uids', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uids', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uids', Keys.BACKSPACE)
        ByIdSendKey(driver, 'deviceConnectionInput_uids', UIDs)

        ByIdClicking(driver, 'deviceConnectionButtonDone')

    def AddServerTag(self, driver, IDnum,addr, Group_name, Device_name, tag_name, valueType):
        # add the detail
        ByIdClicking(driver, 'datamapperAdd')
        # Id
        ByIdSendKey(driver, 'datamapperId_0', IDnum)
        # Type
        ByIdClicking(driver, 'datamapperId_1__BV_toggle_')
        ByIdClicking(driver, 'datamapperId_1_holding')
        # Addr
        ByIdSendKey(driver, 'datamapperId_2', addr)
        # Category
        ByIdClicking(driver, 'datamapperInfo_category__BV_toggle_')
        ByIdClicking(driver, 'datamapperInfo_category_device')
        
        # Group
        ByXpathClicking(driver, f'//*[@id="datamapperInfo_group__BV_toggle_"]')
        ByXpathClicking(driver, f'//*[@id="datamapperInfo_group_{str(Group_name)}"]')

        # Device
        ByIdClicking(driver, f'datamapperInfo_device__BV_toggle_')
        ByXpathClicking(driver, f'//*[@id="datamapperInfo_device_{str(Device_name)}"]')

        # Tag
        ByIdClicking(driver, f'datamapperInfo_tag__BV_toggle_')
        ByIdClicking(driver, f'datamapperInfo_tag_{str(tag_name)}')
    
        # Value Type
        ByIdClicking(driver, f'datamapperInfo_valueType__BV_toggle_')
        ByIdClicking(driver, f'datamapperInfo_valueType_{valueType}')
        # Done
        ByIdClicking(driver, f'datamapperAddDone')

    def AddServerTag100(self, driver, IDnum, addr, Group_name, Device_name, tag_num, valueType):
        # add the detail
        ByIdClicking(driver, 'datamapperAdd')
        # Id
        ByIdSendKey(driver, 'datamapperId_0', IDnum)
        # Type
        ByIdClicking(driver, 'datamapperId_1__BV_toggle_')
        ByIdClicking(driver, 'datamapperId_1_holding')
        # Addr
        ByIdSendKey(driver, 'datamapperId_2', addr)
        # Category
        ByIdClicking(driver, 'datamapperInfo_category__BV_toggle_')
        ByIdClicking(driver, 'datamapperInfo_category_device')
        # Group
        ByIdClicking(driver, 'datamapperInfo_group__BV_toggle_')
        ByIdClicking(driver, f'datamapperInfo_group_{str(Group_name)}')

        # Device
        ByIdClicking(driver, 'datamapperInfo_device__BV_toggle_')
        ByIdClicking(driver, f'datamapperInfo_device_{str(Device_name)}')
        
        # Tag
        ByIdClicking(driver, 'datamapperInfo_tag__BV_toggle_')
        ByXpathClicking(driver, f'/html/body/div[1]/div[2]/div/div[2]/div/body/div/main/div/div[5]/div[2]/div/form/table/tbody/tr[3]/td[8]/div/div/ul/li[{tag_num}]/a')
        # //*[@id="datamapperInfo_tag_"9550"_uint"]
        # ByIdClicking(driver, f'datamapperInfo_tag_{str(tag_name)}')
    
        # Value Type
        ByIdClicking(driver, 'datamapperInfo_valueType__BV_toggle_')
        ByIdClicking(driver, f'datamapperInfo_valueType_{valueType}')
        # Done
        ByIdClicking(driver, 'datamapperAddDone')