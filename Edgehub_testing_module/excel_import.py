from Edgehub_testing_module import selenium_method, crolling
from selenium import webdriver
import pandas as pd
import os

def export():
    df = crolling.DataScarp()
    with pd.ExcelWriter('C:\\Users\\dsshin\\Desktop\\ServerTags.xlsx', index=False) as writer:
        df.to_excel(writer)

if __name__ == "__main__":
    export()