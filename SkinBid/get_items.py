from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import sqlite3
import get_urls
import re

def get_items(url, driver, pages, min_price, max_price):
    conn = sqlite3.connect('../Gp/items.db')
    c = conn.cursor()

    urls = get_urls.get_urls(url, driver, pages, min_price, max_price)
    print(len(urls))

    for url in urls:
        driver.get(url)
        time.sleep(0.5)
        
        try:
            btn = driver.find_element(By.XPATH, '//*[@id="mat-dialog-1"]/app-news-modal/div/app-skb-modal-button/div')
            btn.click()
        except NoSuchElementException:
            pass
        time.sleep(1)
        try:
            btn = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-notifications-permissions-prompt-modal/div/app-skb-modal-button/div')
            btn.click()
        except NoSuchElementException:
            pass
        time.sleep(1)
        try:
            title = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-auction-page/div/div[2]/div[3]/div[5]/div/div[1]').text
            title = title.split(" ")
            desc = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-auction-page/div/div[2]/div[3]/div[5]/div/div[2]').text
            name = title[len(title) - 1] + " " + desc
        except NoSuchElementException:
            name = "none"
        time.sleep(0.1)
        try:
            # price = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-auction-page/div/div[2]/div[3]/div[5]/div/div[9]/button/div').text
            # price = driver.find_element(By.CLASS_NAME, 'flex.items-center.ng-tns-c187-0').text
            price = driver.find_element(By.CLASS_NAME, 'buy-now-button').text
        except NoSuchElementException:
            price = "Checkout € 0.00"
        date_fetched = datetime.now().strftime("%d_%m_%Y")
        try:
            if driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-auction-page/div/div[2]/div[3]/div[5]/div/div[9]/div/button').text == 'Make an offer':
                bargian = True
            else:
                bargian = False
        except NoSuchElementException:
            bargian = False
        try:
            # market_trend = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-auction-page/div/div[2]/div[3]/div[5]/div/div[6]/div[2]/div[2]/div').text
            market_trend = driver.find_element(By.CLASS_NAME, 'white.ng-tns-c187-0.ng-star-inserted').text
        except NoSuchElementException:
            market_trend = "0.00"
        try:
            wear = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-auction-page/div/div[2]/div[3]/div[5]/div/div[3]/div[1]/div[2]').text
        except NoSuchElementException:
            wear = "None"
        
        if len(price) != 0:
            price = re.findall("\d+\.\d+|\d+", price)
            price = float(price[0])
        else:
            price = 0.00

        market_trend = re.findall("\d+\.\d+|\d+", market_trend)
        if len(market_trend) != 0:
            market_trend = float(market_trend[0])
        else:
            market_trend = 0.00
        try:
            percent_diff = round(1-(float(market_trend)/price), 2)
        except ZeroDivisionError as e:
            percent_diff = 0000
            print(e)
        
        # print(name)
        # print(wear)
        # print(price)
        # print(market_trend)
        # print(percent_diff)
        # print(bargian)
        # print(url)
        
        c.execute('INSERT INTO skinbid VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(name, wear, price, market_trend, percent_diff, bargian, url, date_fetched))

        conn.commit()