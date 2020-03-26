from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium_method
import pandas as pd

# Tag
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[3]/td[2]/div/p
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[22]/td[2]/div/p
# start Addr
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[3]/td[3]/div/div/p
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[22]/td[3]/div/div/p
# Length
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[3]/td[4]/div/div/p
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[22]/td[4]/div/div/p
# Value Type
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[3]/td[5]/div/div/p
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[22]/td[5]/div/div/p
# interval
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[3]/td[6]/div/p
# //*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[22]/td[6]/div/p

def Tag_interval(num):
    out = []
    try:
        for i in range(3, 23):
            name = f'//*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[{i}]/td[{num}]/div/p'
            txt = chrome.find_element(By.XPATH, name).text
            out.append(txt)
    except:
        return out

    return out

def other(num):
    out = []
    try:
        for i in range(3,23):
            name = f'//*[@id="navExpandMain"]/div[5]/div[2]/div/form/table/tbody/tr[{i}]/td[{num}]/div/div/p'
            txt = chrome.find_element(By.XPATH, name). text
            out.append(txt)
    except:
        return out

    return out

def DataScarp():
    chrome = webdriver.Chrome()
    chrome.get('http://localhost:1290/device?category=device&name=ingress&line=MLCC%231&index=0')

    tag, addr, length, valueType, interval = Tag_interval(2), other(3), other(4), other(5), Tag_interval(6)
    data = {
        'tag':tag,
        'addr':addr,
        'length':length,
        'valueType':valueType,
        'interval':interval
    }
    selenium_method.ByXpathClicking(chrome, '//*[@id="navExpandMain"]/div[5]/div[2]/div/div/div[1]/nav/ul/li[11]')

    df = pd.DataFrame(data)

    for i in range(10):
        try:
            tag, addr, length, valueType, interval = Tag_interval(2), other(3), other(4), other(5), Tag_interval(6)
            data = {
                'tag':tag,
                'addr':addr,
                'length':length,
                'valueType':valueType,
                'interval':interval
            }
            selenium_method.ByXpathClicking(chrome, '//*[@id="navExpandMain"]/div[5]/div[2]/div/div/div[1]/nav/ul/li[11]')

            df2 = pd.DataFrame(data)
            df = df.append(df2, ignore_index=True)
        except:
            chrome.quit()
            return df
            
    chrome.quit()
    return df

if __name__ == "__main__":
    DataScarp()    