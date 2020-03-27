# -*- coding:utf-8 -*-
import time
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling
import pandas as pd

#ret = fuzzer_method.fuzz(max_length=23)

def DeviceTesting(start):
    for xnum in range(100):
        dv = fuzzer_method.fuzz(max_length=19)
        start.AddDevice(driver)
        time.sleep(0.1)
        start.TypeString(driver, str(dv))
        start.Confirm(driver)
        start.AddDeviceDetail(driver, str(dv), str(dv), 1)
    # for num in range(11):
    #     start.AddDeviceTag(driver, str(num))

    # for j in range(2,7):
    #     ret2 = start.AddDeviceOfDevice(driver, str(dv))
    #     start.Confirm(driver)
    #     start.AddDeviceDetail(driver, str(dv), str(ret2), j)
    #     time.sleep(0.1)
    #     for i in range(5):
    #         start.AddDeviceTag(driver, str(i))
    
    return dv

def ServerTesting(start, dv):
    for i in range(3):
        start.AddServer(driver)
        start.AddServerDetail(driver)
        # for j in range(1,3):
        #     start.AddServerTag(driver, j, "MLCC#1", "ingress",tag, valType)

if __name__ == "__main__":

    # """ Init Chrome Driver and Selenium """
    chrome = selenium_method.InitDriver()
    driver = chrome.SetChrome()
    driver.get('localhost:1290')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    # running time measure
    start_time = time.time()
    print("Start time: ", start_time)

    # start.ConfigureClear(driver)
    data = crolling.DataScarp()
    # print(data)
    start.AddServer(driver)
    start.AddServerDetail(driver)
    for i in range(len(data)-1):
        if len(data) <= 50:
            start.AddServerTag(driver, i+1, "MLCC#1", "ingress",data['tag'][i], data['valueType'][i])
        else:
            start.AddServerTag100(driver, i+1, "MLCC#1", "ingress", i+1 , data['valueType'][i])

    # dv = DeviceTesting(start)
    # ServerTesting(start, dv)
    # start.Commit(driver)

    print("consuming time:", time.time() - start_time)

    #driver.quit()
