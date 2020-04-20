# -*- coding:utf-8 -*-
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling, Device_module

if __name__ == "__main__":
    chrome = selenium_method.InitDriver()
    driver = chrome.SetChrome()
    
    driver.get("http://localhost:1290/device?category=device&name=d&line=g&index=0")
    
    for i in range(1,1000):
        selenium_method.ByIdClicking(driver, f'datamapperAdd')
        selenium_method.ByIdSendKey(driver, f'datamapperId_0', str(i))
        selenium_method.ByIdSendKey(driver, f'datamapperInfo_id', str(1))
        selenium_method.ByIdSendKey(driver, f'datamapperInfo_address', str(i))
        selenium_method.ByIdSendKey(driver, f'datamapperInfo_length', str(1))

        selenium_method.ByIdClicking(driver, f'datamapperInfo_valueType__BV_toggle_')
        selenium_method.ByIdClicking(driver, f'datamapperInfo_valueType_int')

        selenium_method.ByIdSendKey(driver, f'datamapperInterval', str(1000))

        selenium_method.ByIdClicking(driver, f'datamapperAddDone')

    

    