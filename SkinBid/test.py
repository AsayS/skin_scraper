from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.common.exceptions import NoSuchElementException
import time


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = 'https://skinbid.com/market/81a2918b-d3e2-43f3-bca3-4273ffce6855/stattraktm-p250-muertos-minimal-wear'
min_price = "2"
max_price = "=35"
page = 30
url = f'https://skinbid.com/listings?Pricegt={min_price}Pricelt{max_price}&Wear=FactoryNew,MinimalWear,FieldTested&goodDeals=false&sort=created%23desc&skip=' + str(page) + '&take=30&sellType=fixed_price'

driver.get(url)

# does not include souvenier in the name even if it is a souvenier item
try:
    name = driver.find_element(By.CLASS_NAME, 'item-title').text
    price = driver.find_element(By.CLASS_NAME, 'buy-now-button').text
    market_price = driver.find_element(By.CLASS_NAME, 'white.ng-tns-c187-0.ng-star-inserted').text
except NoSuchElementException:
    name = "none"
    price = "none"
print(name)
print(price)
print(market_price)


# import sqlite3

# conn = sqlite3.connect('../Gp/items.db')


# c = conn.cursor()

# # c.execute("""CREATE TABLE skinbid (
# #                 name text,
# #                 wear text,
# #                 price real,
# #                 market_price real,
# #                 percent_diff real,
# #                 bargian text,
# #                 url text,
# #                 date text
# #                 )""")



# c.execute("DELETE FROM skinbid WHERE bargian LIKE 'False'")

# # c.execute("DROP TABLE skinbid")

# conn.commit()
# conn.close()