# -*- UTF-8 encoding -*-
import time
import selenium_method
import fuzzer_method

#ret = fuzzer_method.fuzz(max_length=23)

chrome = selenium_method.InitDriver()
driver = chrome.SetChrome()
driver.get('localhost:1290')

start = selenium_method.AddToContents()
start.ConfigureClear(driver)

# running time measure
start_time = time.time()

start.AddDevice(driver)
start.TypeString(driver, "Device_01")
start.Confirm(driver)

start.AddDeviceOfDevice(driver, "Device_01")
start.Confirm(driver)

start.AddDeviceDetail(driver, "Device_01")
for i in range(200):
    start.AddDeviceTag(driver, str(i))

print("consuming time:", time.time() - start_time)
#driver.quit()
