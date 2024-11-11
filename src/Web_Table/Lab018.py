import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from src.EX_24102024.test_SVG_lab016 import driver


def test_webTable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    web_element = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(web_element)

    print(col)

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_prat = "]/td"
    third_part = "]"

    for i in range(2, row +1):
        for j in range (1, col+1):
            dynamic


