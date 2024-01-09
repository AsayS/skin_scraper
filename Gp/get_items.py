from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
from datetime import datetime
import sqlite3


def get_items(url, driver):
    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    driver.get(url)

    time.sleep(2)

    items = driver.find_elements(By.CLASS_NAME, 'ItemCardNew_container__aCPda')

    time.sleep(1)

    for item in items:
        try:
            name = item.find_element(By.CLASS_NAME, 'ItemCardNewBody_name__VV0vu').text
        except NoSuchElementException:
            name = "none"
        try:
            price = item.find_element(By.CLASS_NAME, 'ItemCardNewBody_pricePrimary__Tpkw7').text
        except NoSuchElementException:
            price = 0
        try:
            url = item.find_element(By.CLASS_NAME, 'ItemCardNewBody_bottom__CpdbV > a').get_attribute('href')
        except NoSuchElementException:
            url = "none"
        date_fetched = datetime.now().strftime("%d_%m_%Y")
        try:
            if item.find_element(By.CLASS_NAME, 'ItemCardNew_buttonBargain__CQj02').text == "Bargain":
                bargian = True
            else:
                continue
        except NoSuchElementException:
            bargian = False
        try:
            buff_price = item.find_element(By.CLASS_NAME, 'ItemCardNewBody_buffPrice__ozHP4').text
        except NoSuchAttributeException:
            buff_price = 000
        
        # print(str(name))
        # print(str(price))
        # print(str(buff_price))
        # print(str(bargian))
        # print(str(url))
        # print(str(date_fetched))
        c.execute('INSERT INTO items VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'.format(name, price, buff_price, bargian, url, date_fetched))
        
    conn.commit()
    conn.close()
    
