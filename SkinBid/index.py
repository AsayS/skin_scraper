from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import login
import get_items
# min_price, max_price, first_page, pages

# TODO make input args with error handling from command line
# TODO auto get ids from buff_ids.txt file 
def index(min_price, max_price, pages):
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    url = ""
    login.logins(driver)
    get_items.get_items(url, driver, pages, min_price, max_price)
    # driver.maximize_window()
    # login.logins(driver)
    # pages = pages + 1
    
index(1.5, 35, 20)