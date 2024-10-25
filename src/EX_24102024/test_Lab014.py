import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_Alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_Alert.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(3)

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You successfully clicked an alert"

def test_alerts_js_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_Confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_Confirm.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.dismiss()
    time.sleep(3)
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You clicked: Cancel"

def test_alerts_js_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_Prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_Prompt.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.send_keys("Prachi")
    alert.accept()
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: Prachi"