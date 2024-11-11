import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.title("Action 2")
@allure.description("verify action 2")
def test_verify_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    # //input[@name="firstname"]
    # input[name="firstname"]
    # By.Name -> firstNAME

    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")

    # KEY_DOWN
    actions = ActionChains(driver=driver)
    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(last_name, "the testing academy")
     .key_up(Keys.SHIFT).perform()
     )

    time.sleep(10)
    driver.quit()