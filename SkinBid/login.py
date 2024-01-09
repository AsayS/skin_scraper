from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import configparser

config_object = configparser.ConfigParser()
with open("../login.ini","r") as file_object:
    config_object.read_file(file_object)
    password=config_object.get("login","password")
    username=config_object.get("login","username")

def logins(driver):
    driver.get('https://www.steamcommunity.com/')
    element = driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a[2]')
    element.click()
    time.sleep(2.5)
    element = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
    element.send_keys(str(username))

    time.sleep(3)

    element = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
    element.send_keys(str(password))

    time.sleep(4)

    element = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button')
    element.click()

    time.sleep(4)

    driver.get('https://www.skinbid.com')
    
    element = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-header/div/div/div[3]/div/a')
    element.click()
    
    time.sleep(4)
    
    element = driver.find_element(By.XPATH, '//*[@id="imageLogin"]')
    element.click()
    
    time.sleep(5)
    
    driver.get('https://skinbid.com/listings?Pricelt=35&Wear=FactoryNew,MinimalWear,FieldTested&goodDeals=true&sort=discount%23desc&skip=0&take=30&sellType=fixed_price')
    
    time.sleep(5)
    try:
        element = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-steam-keys-setup-page/div/button')
        element.click()
    except NoSuchElementException:
        return
    time.sleep(2)
    
