# -*- coding:utf-8 -*-
import time
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import psutil
import pandas as pd


def once(start, driver, iter, interval, df, ret):
    
    # running time measure
    # start_time = time.time()
    # print("Start time: ", start_time)
    
    # first time create device group and device
    start.ConfigureClear(driver)
    start.AddDevice(driver)
    start.TypeString(driver, ret)
    start.Confirm(driver)

    # Commit
    # start.Commit(driver)

    # Device name, Device group name, UID, addr, port, connection count, interval
    start.AddDeviceDetail(driver, ret, ret, 55, '127.0.0.1', 502, 1, 1000)

    for i in range(iter):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], str(interval))
    
    # server add
    start.AddServer(driver)

    # Server Uids, port
    UIDs = 55
    port = 503
    start.AddServerDetail(driver, str(UIDs), str(port))
    
    # server tag add
    for i in range(iter):
        if len(df) <= 50:
            # driver, IDnum, addr, Group_name, Device_name, tag_name, valueType
            start.AddServerTag(driver, UIDs, i+1, ret , ret, df['tag'][i] , df['valueType'][i])
        else:
            # driver, IDnum, addr, Group_name, Device_name, tag_name, valueType
            start.AddServerTag100(driver, UIDs, i+1, ret, ret, i+1 , df['valueType'][i])

    # start.Commit(driver)

    # print("consuming time:", time.time() - start_time)

    #driver.quit()

def checkData(start, driver):
    time.sleep(3)
    data = []
    for i in range(8):
        for num in range(3, 23):
            try:
                txt = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[2]/div/body/div/main/div/div[5]/div[2]/div/form/table/tbody/tr[{num}]/td[12]/div/p').text
                if txt == '':
                    data.append('NoData')
                else: 
                    data.append(txt)
            except:
                print("end")
                driver.quit()
                return data

        selenium_method.ByXpathClicking(driver, '//*[@id="navExpandMain"]/div[5]/div[2]/div/div/div[1]/nav/ul/li[11]')
        time.sleep(0.1)
    return data

if __name__ == "__main__":

    # df = pd.read_excel('ServerTags.xlsx', index=False)
    # del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome = selenium_method.InitDriver()
    driver = chrome.SetChrome()
    driver.get('http://localhost:1290/device?category=device&name=xaglruailxl&line=xaglruailxl&index=0')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    count = 0
    # once(start, driver, len(df)-1, 1000, df, ret)
    Results = pd.DataFrame({"result":checkData(start, driver)})
    print(Results['result'])
    for i in range(len(Results)):
        if Results['result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(count)