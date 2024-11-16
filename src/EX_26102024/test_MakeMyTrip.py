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
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=5).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    )

    close_popup = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    time.sleep(3)
    close_popup.click()

    From_city= driver.find_element(By.ID, "fromCity")
    From_city.click()
    actions =ActionChains(driver)
    (actions.move_to_element(From_city)
     .click().send_keys("del")
     .perform()
     )

    time.sleep(2)
    actions.move_to_element(From_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(5)
    driver.quit()