from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException

from get_items import get_items



def url_adjustor(min_price, max_price, pages):
    pages = pages + 1
    for i in range(1, pages):
        url = 'https://gamerpay.gg/?priceMin=' + str(min_price) + '&priceMax=' +str(max_price)+ '&tradeLocked=0&wear=Field-Tested%2CMinimal+Wear%2CFactory+New&page='+str(i)+'&sortBy=deals&ascending=true'
        get_items(url)
        
url_adjustor(100, 3000, 4)








# url = 'https://gamerpay.gg/?priceMin=300&priceMax=3000&tradeLocked=0&wear=Field-Tested%2CMinimal+Wear%2CFactory+New&page=1&sortBy=deals&ascending=true'

# driver.get(url)

