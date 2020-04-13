from Edgehub_testing_module import fuzzer_method, selenium_method
import time
import pandas as pd

def checkData(start, driver, localhost, check_name):
    driver.get(f'{localhost}' + f'{check_name}')
    # Wait for yield the Web page
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
                # print("end")
                # driver.quit()
                return data

        selenium_method.ByXpathClicking(driver, '//*[@id="navExpandMain"]/div[5]/div[2]/div/div/div[1]/nav/ul/li[11]')
        time.sleep(0.1)
    return data

def init():
    chrome = selenium_method.InitDriver()
    driver = chrome.SetChrome()
    return chrome, driver

def modTCP(start, driver, ret, df,
    interation = 10,
    interval = 1000,
    Device_UID = 55,
    Device_addr = '127.0.0.1',
    Device_port = 502,
    Device_count = 1,
    Device_TimeOut = 1000):
    
    # running time measure
    # start_time = time.time()
    # print("Start time: ", start_time)
    
    # first time create device group and device
    # start.ConfigureClear(driver)
    start.AddDevice(driver, ret)

    # Commit
    # start.Commit(driver)
    
    # Device name, Device group name, UID, addr, port, connection count, interval
    start.AddDeviceDetail_TCP(driver, ret, ret, Device_UID, Device_addr, Device_port, Device_count, Device_TimeOut)

    for i in range(interation):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], str(interval))
    
    # server add
    # start.AddServer(driver, ret)

    # # Server Uids, port
    # server_UIDs = 55
    # server_port = 503
    # start.AddServerDetail(driver, str(server_UIDs), str(server_port))
    
    # # server tag add
    # for i in range(iter):
    #     if len(df) <= 50:
    #         # driver, IDnum, addr, Group_name, Device_name, tag_name, valueType
    #         start.AddServerTag(driver, server_UIDs, i+1, ret , ret, df['tag'][i] , df['valueType'][i])
    #     else:
    #         # driver, IDnum, addr, Group_name, Device_name, tag_name, valueType
    #         start.AddServerTag100(driver, server_UIDs, i+1, ret, ret, i+1 , df['valueType'][i])

    # start.Commit(driver)

    # print("consuming time:", time.time() - start_time)

    #driver.quit()

def ModbusTCP_test(dv, dt):
    # croll a excel data which involving a server tags
    df = pd.read_excel('ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome, driver = init()
    
    localhost = f'http://localhost:1290'
    check_name = f'/device?category=device&name={ret}&{ret}&line={ret}&index=0'
    
    driver.get(f'{localhost}')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    # start, driver, iter, interval, df, ret, Device_UID = 55, Device_addr = '127.0.0.1', Device_port = 502, Device_count = 1, Device_TimeOut = 1000
    Device_UID = 55
    Device_interval = dv
    Device_addr = '127.0.0.1'
    Device_port = 502
    Device_count = 1
    Device_TImeOut = dt
    
    modTCP(start, driver, ret, df, 10, Device_interval, Device_UID, Device_addr, Device_port, Device_count, Device_TImeOut)

    start.Commit(driver)
    time.sleep(5)

    # get page index of Device tags
    driver.get(f'{localhost}' + f'{check_name}')
    count = 0
    Results = pd.DataFrame({"ModbusTCP_result":checkData(start, driver, localhost, check_name)})
    # print(Results['result'])
    for i in range(len(Results)):
        if Results['ModbusTCP_result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(f'[*] ModbusTCP success data results: {count}')
    print(f'[!] driver quit')
    driver.quit()

    # print(f'[!] measuring CPU/MEM usage of the erl process for 5 seconds. Please wait.')
    # for proc in psutil.process_iter(['name']):
    #     if proc['name'] == 'erl':
    #         print(proc.info)
    

    return Results

def ModRTU(start, driver, ret, df, iteration = 10):
    # start.ConfigureClear(driver)
    start.AddDevice(driver, ret)
    start.AddDeviceDetail_RTU(driver, ret, ret)

    for i in range(iteration):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], 1000)

def ModbusRTU_test():
    # croll a excel data which involving a server tags
    df = pd.read_excel('ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome, driver = init()
    
    localhost = f'http://localhost:1290'
    check_name = f'/device?category=device&name={ret}&{ret}&line={ret}&index=0'
    
    driver.get(f'{localhost}')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    ModRTU(start, driver, ret, df, 10)

    start.Commit(driver)
    time.sleep(5)

    # get page index of Device tags
    driver.get(f'{localhost}' + f'{check_name}')
    count = 0
    Results = pd.DataFrame({"ModbusTCP_result":checkData(start, driver, localhost, check_name)})
    # print(Results['result'])
    for i in range(len(Results)):
        if Results['ModbusTCP_result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(f'[*] ModbusRTU success data results: {count}')
    print(f'[!] driver quit')
    driver.quit()

    return Results

def Cnet(start, driver, ret, df, interation = 10):
    # start.ConfigureClear(driver)
    start.AddDevice(driver, ret)
    start.AddDeviceDetail_CNET(driver, ret, ret)

    for i in range(interation):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], 1000)
  
def Cnet_test():
    # croll a excel data which involving a server tags
    df = pd.read_excel('ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome, driver = init()
    
    localhost = f'http://localhost:1290'
    check_name = f'/device?category=device&name={ret}&{ret}&line={ret}&index=0'
    
    driver.get(f'{localhost}')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    Cnet(start, driver, ret, df, 10)

    start.Commit(driver)
    time.sleep(5)

    # get page index of Device tags
    driver.get(f'{localhost}' + f'{check_name}')
    count = 0
    Results = pd.DataFrame({"ModbusTCP_result":checkData(start, driver, localhost, check_name)})
    # print(Results['result'])
    for i in range(len(Results)):
        if Results['ModbusTCP_result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(f'[*] CNET success data results: {count}')
    print(f'[!] driver quit')
    driver.quit()

    return Results

def Fenet(start, driver, ret, df, interation = 10):
    # start.ConfigureClear(driver)
    start.AddDevice(driver, ret)
    start.AddDeviceDetail_FENET(driver, ret, ret)

    for i in range(interation):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], 1000)

def Fenet_test():
    # croll a excel data which involving a server tags
    df = pd.read_excel('ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome, driver = init()
    
    localhost = f'http://localhost:1290'
    check_name = f'/device?category=device&name={ret}&{ret}&line={ret}&index=0'
    
    driver.get(f'{localhost}')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    Fenet(start, driver, ret, df, 10)

    start.Commit(driver)
    time.sleep(5)

    # get page index of Device tags
    driver.get(f'{localhost}' + f'{check_name}')
    count = 0
    Results = pd.DataFrame({"ModbusTCP_result":checkData(start, driver, localhost, check_name)})
    # print(Results['result'])
    for i in range(len(Results)):
        if Results['ModbusTCP_result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(f'[*] FENET success data results: {count}')
    print(f'[!] driver quit')
    driver.quit()

    return Results

def MELSEC_SERIAL(start, driver, ret, df, interation = 10):
    # start.ConfigureClear(driver)
    start.AddDevice(driver, ret)
    start.AddDeviceDetail_MELSEC_SERIAL(driver, ret, ret)

    for i in range(interation):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], 1000)

def MELSEC_SERIAL_test():
    # croll a excel data which involving a server tags
    df = pd.read_excel('ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome, driver = init()
    
    localhost = f'http://localhost:1290'
    check_name = f'/device?category=device&name={ret}&{ret}&line={ret}&index=0'
    
    driver.get(f'{localhost}')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    MELSEC_SERIAL(start, driver, ret, df, 10)

    start.Commit(driver)
    time.sleep(5)

    # get page index of Device tags
    driver.get(f'{localhost}' + f'{check_name}')
    count = 0
    Results = pd.DataFrame({"ModbusTCP_result":checkData(start, driver, localhost, check_name)})
    # print(Results['result'])
    for i in range(len(Results)):
        if Results['ModbusTCP_result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(f'[*] MELSEC_SERIAL success data results: {count}')
    print(f'[!] driver quit')
    driver.quit()

    return Results

def MELSEC_ETH(start, driver, ret, df, interation = 10):
    # start.ConfigureClear(driver)
    start.AddDevice(driver, ret)
    start.AddDeviceDetail_MELSEC_ETHERNET(driver, ret, ret)

    for i in range(interation):
        # tag, addr, length, valuetype, interval
        start.AddDeviceTag(driver, df['tag'][i], df['addr'][i], df['length'][i], df['valueType'][i], 1000)
    
def MELSEC_ETH_test():
    # croll a excel data which involving a server tags
    df = pd.read_excel('ServerTags.xlsx', index=False)
    del df['Unnamed: 0']
    # print(len(df))
    # print(df)

    ret = fuzzer_method.fuzz(max_length=20)

    # """ Init Chrome Driver and Selenium """
    chrome, driver = init()
    
    localhost = f'http://localhost:1290'
    check_name = f'/device?category=device&name={ret}&{ret}&line={ret}&index=0'
    
    driver.get(f'{localhost}')

    # Create object that selenium running module
    start = selenium_method.AddToContents()

    MELSEC_ETH(start, driver, ret, df, 10)

    start.Commit(driver)
    time.sleep(5)

    # get page index of Device tags
    driver.get(f'{localhost}' + f'{check_name}')
    count = 0
    Results = pd.DataFrame({"ModbusTCP_result":checkData(start, driver, localhost, check_name)})
    # print(Results['result'])
    for i in range(len(Results)):
        if Results['ModbusTCP_result'][i] == 'NoData':
            pass
        else:
            count += 1
    print(f'[*] MELSEC_ETHERNET success data results: {count}')
    print(f'[!] driver quit')
    driver.quit()

    return Results
    
def OPC_UA():
    return True

def OPC_UA_test():
    return True

def https():
    return True

def https_test():
    return True
