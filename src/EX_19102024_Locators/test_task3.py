import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Register Account")
@allure.description("Verify that successfully Register Account")
def test_open_Register_Account():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    enter_firstname = driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    enter_firstname.send_keys("Prachi")
    time.sleep(3)
    enter_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    enter_lastname.send_keys("Yelkar")
    time.sleep(3)
    enter_email = driver.find_element(By.ID, "input-email")
    enter_email.send_keys("prachicleartest123@gmail.com")
    time.sleep(3)
    enter_telephone = driver.find_element(By.NAME, "telephone")
    enter_telephone.send_keys("8452632515")
    time.sleep(3)
    enter_password = driver.find_element(By.XPATH, "//input[@name='password']")
    enter_password.send_keys("Prachi@123")
    time.sleep(3)
    enter_confirm_password = driver.find_element(By.XPATH, "//input[@name='confirm']")
    enter_confirm_password.send_keys("Prachi@123")
    time.sleep(3)
    subscribe_newsletter = driver.find_element(By.XPATH, "(.//input[@value='1'])[2]")
    subscribe_newsletter.click()
    time.sleep(3)
    check_privacy_policy = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    check_privacy_policy.click()
    time.sleep(3)
    btn_continue = driver.find_element(By.XPATH, "//*[@type='submit']")
    btn_continue.click()
    time.sleep(3)
    success_message = driver.find_element(By.XPATH, "//div/h1").text
    print("Title of the Page is: ", driver.title)
    print("Text to be validated is: ", success_message)
    assert success_message.__eq__("Your Account Has Been Created!")

    time.sleep(5)