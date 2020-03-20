# -*- UTF-8 encoding -*-
import time
import selenium_method
import fuzzer_method

#ret = fuzzer_method.fuzz(max_length=23)

def DeviceTesting(start):
    dv = fuzzer_method.fuzz(10)
    start.AddDevice(driver)
    start.TypeString(driver, str(dv))
    start.Confirm(driver)
    start.AddDeviceDetail(driver, str(dv), str(dv))
    for num in range(200):
        start.AddDeviceTag(driver, str(num))

    ret2 = start.AddDeviceOfDevice(driver, str(dv))
    start.Confirm(driver)
    start.AddDeviceDetail(driver, str(dv), str(ret2))
    for i in range(200):
        start.AddDeviceTag(driver, str(i))
    
    return dv

def ServerTesting(start, dv):
    for i in range(200):
        start.AddServer(driver)
        start.AddServerDetail(driver)
        for j in range(200):
            start.AddServerTag(driver, j, dv)

if __name__ == "__main__":

    chrome = selenium_method.InitDriver()
    driver = chrome.SetChrome()
    driver.get('localhost:1290')

    start = selenium_method.AddToContents()
    start.ConfigureClear(driver)

    # running time measure
    start_time = time.time()
    print("Start time: ", start_time)

    dv = DeviceTesting(start)
    ServerTesting(start, dv)
    start.Commit(driver)

    print("consuming time:", time.time() - start_time)

    #driver.quit()
