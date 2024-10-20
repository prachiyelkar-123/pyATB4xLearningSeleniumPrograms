import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import allure
from selenium.webdriver.common.by import By


@pytest.mark.negative
@allure.title("test_start_free_trile")
@allure.description("Verify that if start_free_trile link is cliackable or not")
def test_start_free_trile_project3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")


#link tag
    anchare_tag = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchare_tag.click()

    # PARTIAL_LINK_TEXT - contains
    #anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    #anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.back()


    time.sleep(3)