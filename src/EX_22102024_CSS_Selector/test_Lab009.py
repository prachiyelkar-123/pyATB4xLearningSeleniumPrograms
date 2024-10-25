import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")

def test_task5():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_box.send_keys("macmini")
    search_btn = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    search_btn.click()
    driver.implicitly_wait(10)
    # Capture titles, price and store them in list
    list_of_products = driver.find_elements(By.XPATH, "(//span[@role='heading'])[position()>2]")

    list_of_price = driver.find_elements(By.XPATH, "(.//div/span[@class='s-item__price'] )[position()>2]")

    for i in list_of_products:
        l.append(i.text)
    for j in list_of_price:
        p.append(j.text)
    # Print titles and price
    print(l)
    print(p)
    # Convert the price values to float in order to get max and min price by list comprehention
    p_val = [val.replace('$', '').replace(' to ', ',') for val in p]
    p_val1 = [val1.split(',') for val1 in p_val]

    print(p_val1)
    new_list = [float(item) for sublist in p_val1 for item in sublist]
    print(new_list)

    max_pval = max(new_list)
    min_pval = min(new_list)

    print(f"Max value in price list is: {max_pval}")
    print(f"Min value in price list is: {min_pval}")

    print(len(l))
    print(len(new_list))
    # Use zip function to join two lists and show in dictionary format
    title_n_price = dict(zip(l, new_list))
    print(f"Title and Price of the products is : {title_n_price}")
    driver.quit()