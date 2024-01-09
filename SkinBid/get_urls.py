from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

urls = []

def get_urls(url, driver, pages, min_price, max_price):
    time.sleep(2)
    for i in range(pages):
        page = i * 30
        url = f'https://skinbid.com/listings?Pricegt={str(min_price)}&Pricelt={str(max_price)}&Wear=FactoryNew,MinimalWear,FieldTested&goodDeals=false&sort=created%23desc&skip=' + str(page) + '&take=30&sellType=fixed_price'
        driver.get(url)
        
        time.sleep(1)
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
        try:
            element = driver.find_element(By.XPATH, '//*[@id="mat-dialog-1"]/app-news-modal/div/app-skb-modal-button')
            element.click
        except NoSuchElementException:
            pass
        time.sleep(0.5)
        try:
            everythin = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-search-page/div/div[2]/div[4]/div[2]/div')
        except NoSuchElementException:
            pass

        items = everythin.find_elements(By.CLASS_NAME, 'item.ng-tns-c194-0.ng-trigger.ng-trigger-fadeIn')
            
        time.sleep(1)
        
        for item in items:
            url = item.find_element(By.CLASS_NAME, 'content').get_attribute('href')
            urls.append(url)
        print(len(urls))
    return urls

    
