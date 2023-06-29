from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''
Test of an authorization form at saucedemo.com
'''

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


def get_driver():  # Configuring Chrome and installing webdriver for Chrome
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,800')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def open_page(driver: webdriver, url: str):  # Opening our URL
    driver.get(url)


def get_element_by_id(driver: webdriver, id: str):  # Choosing element for interaction by its ID
    return driver.find_element(By.ID, id)


def element_click_by_id(driver: webdriver, id: str):  # Creating a click event on chosen element
    element = get_element_by_id(driver, id)
    element.click()


def element_send_keys_by_id(driver: webdriver, id: str, text: str):  # Typing text in a chosen element
    element = get_element_by_id(driver, id)
    element.send_keys(text)


def login(driver: webdriver, login: str, password: str):  # Filling authorization form with our login and password
    element_send_keys_by_id(driver, 'user-name', login)
    element_send_keys_by_id(driver, 'password', password)
    element_click_by_id(driver, 'login-button')


def quit(driver: webdriver):  # Quitting webdriver
    driver.quit()


driver = get_driver()
open_page(driver, URL)
login(driver, login=LOGIN, password=PASSWORD)

quit(driver)
