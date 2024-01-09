from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

import login
import get_items

def url_adjustor(min_price, max_price, first_page, pages):
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    login.logins(driver)
    pages = pages + 1
    for i in range(first_page, pages):
        url = 'https://gamerpay.gg/?priceMin=' + str(min_price) + '&priceMax=' +str(max_price)+ '&tradeLocked=0&wear=Field-Tested%2CMinimal+Wear%2CFactory+New&page='+str(i)+'&sortBy=deals&ascending=true'
        get_items.get_items(url, driver)
        
url_adjustor(100, 3000, 1, 10)