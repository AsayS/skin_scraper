from selenium.webdriver.common.by import By
import time
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

    time.sleep(2)

    element = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button')
    element.click()

    time.sleep(2)

    driver.get('https://www.gamerpay.gg/')

    button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/header[1]/nav/ul[2]/li[3]/button')
    button.click()

    time.sleep(3.5)

    button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/button')
    button.click()

    time.sleep(3.5)

    button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/button')
    button.click()

    time.sleep(2.5)

    button = driver.find_element(By.XPATH, '//*[@id="imageLogin"]')
    button.click()

    time.sleep(1.3)

    
