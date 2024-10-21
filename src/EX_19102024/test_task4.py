import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


def test_selenium_negative_with_class_name():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")
    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")
    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(3)
    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
