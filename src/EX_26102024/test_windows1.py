from asyncio import timeout

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P5")
@allure.description("Verify dropdown")
def test_verify_action_MakeMyTrip():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle
    print(parent_window)

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Testcase Passed!!")
            break


    time.sleep(5)
    driver.quit()
