# -*- coding:utf-8 -*-
import time
<<<<<<< HEAD
from Edgehub_fuzz_module import fuzzer_method, selenium_method

<<<<<<< HEAD

=======
>>>>>>> e522df0575dc60b2666e72e9fd950150488af087
=======
import fuzzer_method, selenium_method
>>>>>>> 5b01135597cbc93fa97bea041dd0a59352674235
#ret = fuzzer_method.fuzz(max_length=23)

def DeviceTesting(start):
    dv = fuzzer_method.fuzz(max_length=19)
    start.AddDevice(driver)
    start.TypeString(driver, str(dv))
    start.Confirm(driver)
    start.AddDeviceDetail(driver, str(dv), str(dv), 1)
    for num in range(13):
        start.AddDeviceTag(driver, str(num))

    for j in range(2,42):
        ret2 = start.AddDeviceOfDevice(driver, str(dv))
        start.Confirm(driver)
        start.AddDeviceDetail(driver, str(dv), str(ret2), j)
        time.sleep(0.1)
        for i in range(13):
            start.AddDeviceTag(driver, str(i))
    
    return dv

def ServerTesting(start, dv):
    for i in range(20):
        start.AddServer(driver)
        start.AddServerDetail(driver)
        for j in range(1,21):
            start.AddServerTag(driver, j, dv)

if __name__ == "__main__":

    # """ Init Chrome Driver and Selenium """
    chrome = selenium_method.InitDriver()
    driver = chrome.SetChrome()
    driver.get('localhost:1290')

    # Create object that selenium running module
    start = selenium_method.AddToContents()
    start.ConfigureClear(driver)

    # running time measure
    start_time = time.time()
    print("Start time: ", start_time)

    start.ConfigureClear(driver)
    dv = DeviceTesting(start)
    # ServerTesting(start, dv)
    start.Commit(driver)

    print("consuming time:", time.time() - start_time)

    #driver.quit()
