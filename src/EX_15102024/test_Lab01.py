from selenium import webdriver
import allure
import pytest

@allure.title("verify title of webpage")

def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")
