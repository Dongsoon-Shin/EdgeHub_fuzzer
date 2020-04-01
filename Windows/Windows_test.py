# -*- coding:utf-8 -*-
import time
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling
import pandas as pd

#ret = fuzzer_method.fuzz(max_length=23)

if __name__ == "__main__":

    df = pd.read_excel('C:\\Users\\dsshin\\Desktop\\ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(df['addr'], df['tag'], df['length'], df['valueType'], df['interval'])

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
    # start.AddDevice(driver)
    # start.TypeString(driver, "Test_1000ms")
    # start.Confirm(driver)

    # start.AddDeviceDetail(driver, "Test_1000ms", "Test_1000ms", 55)
    # for i in range(len(df)-1):
    #     start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], str(1000))
    
    start.AddServer(driver)
    start.AddServerDetail(driver)
    for i in range(len(df)-1):
        if len(df) <= 50:
            start.AddServerTag(driver, i+1, "Test_1000ms", "Test_1000ms",df['tag'][i], df['valueType'][i])
        else:
            start.AddServerTag100(driver, i+1, "Test_1000ms", "Test_1000ms", i+1 , df['valueType'][i])

    # start.Commit(driver)

    print("consuming time:", time.time() - start_time)

    #driver.quit()
