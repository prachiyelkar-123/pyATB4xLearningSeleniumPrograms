import time

from selenium import webdriver

def test_open_VWO_login():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    page_source_data = driver.page_source
    print(page_source_data)

    time.sleep(10)