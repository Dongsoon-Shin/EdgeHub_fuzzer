from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('http://localhost:1290/device?category=device&name=ingress&line=MLCC%231&index=0')
