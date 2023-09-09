import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

service_chrome = Service('D:/QA/chromedriver')
driver = webdriver.Chrome(service=service_chrome)

def test():
    # driver.maximize_window()
    driver.get('https://target.my.com')
    WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')))

    elem = driver.find_element(By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    elem.click()
    # webdriver.ActionChains(driver).click(elem).perform() Как альтернатива

    elem2 = driver.find_element(By.NAME, 'email')
    elem2.send_keys('TXMachine@yandex.ru')

    elem3 = driver.find_element(By.NAME, 'password')
    elem3.send_keys('txmachine')

    elem4 = driver.find_element(By.XPATH, '//div[contains(@class,"authForm-module-button")]')
    elem4.click()

def test2():
    WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')))
    elem5 = driver.find_element(By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')
    elem5.click()

    """  
        Я ожидаю пока данный элемент станет кликабельным, но ошибка, что элемент не кликабелен, все равно вылетает  
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[contains(@class, "rightMenu-module-rightMenuLink")]')))
    """
    elem6 = driver.find_element(By.XPATH, '//a[@href="/logout"]')
    time.sleep(3)
    elem6.click()
    time.sleep(3)

