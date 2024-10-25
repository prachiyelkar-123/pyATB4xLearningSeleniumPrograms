import time
import allure
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_task5():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    time.sleep(3)

    enter_firstname = driver.find_element(By.NAME, "firstname")
    enter_firstname.send_keys("Prachi")
    time.sleep(3)

    enter_lastname = driver.find_element(By.XPATH, "//input[@name = 'lastname']")
    enter_lastname.send_keys("Yelkar")

    select_gender = driver.find_element(By.XPATH, "//input[@value = 'Female']")
    select_gender.click()
    time.sleep(3)

    profession_element = driver.find_element(By.XPATH, "//input[@type = 'checkbox' and @value='Automation Tester']")
    profession_element.click()
    time.sleep(3)

    YearOfExp = driver.find_element(By.ID, "exp-2")
    YearOfExp.click()
    time.sleep(3)


