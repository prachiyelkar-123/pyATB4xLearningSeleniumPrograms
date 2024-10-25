from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By


@allure.title("Katalon-cura-demo project login test")
@allure.description("Verifying username/password and Login button functionality")

def test_make_appointment_button_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()
    current_url = driver.current_url
    print(current_url)
    time.sleep(6)
    assert current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    user_name = driver.find_element(By.NAME, "username")
    user_name.send_keys("John Doe")
    user_name = driver.find_element(By.ID, "txt-password")
    user_name.send_keys("ThisIsNotAPassword")

    login_btn = driver.find_element(By.ID, "btn-login")
    login_btn.click()

    current_url = driver.current_url
    print(current_url)
    time.sleep(6)
    assert current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(10)
    driver.quit()