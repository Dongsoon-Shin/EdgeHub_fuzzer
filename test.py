# -*- UTF-8 encoding -*-
import os, inspect, subprocess, random, time
import selenium_method
import fuzzer_method

#ret = fuzzer_method.fuzz(max_length=23)

chrome = selenium_method.InitDriver()
driver = chrome.SetChrome()
driver.get('localhost:1290')

start = selenium_method.AddToContents()
# start.ConfigureClear(driver)

# running time measure
start_time = time.time()

start.AddDevice(driver)
start.TypeString(driver, "Device_01")
start.Confirm(driver)

for i in range(8000):
    start.AddDeviceTag(driver, "Device_01")
    start.Confirm(driver)

print("consuming time:", time.time() - start_time)
driver.quit()