import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_element = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)

    #select.select_by_visible_text("Option 2")
    select.select_by_index(1)
    time.sleep(5)