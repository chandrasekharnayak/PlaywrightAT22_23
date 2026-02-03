from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

#selective dropdown

selective_dropdown = Select(driver.find_element(By.ID,"dropdown-class-example"))
# selective_dropdown.select_by_index(2)
# selective_dropdown.select_by_value("option3")
selective_dropdown.select_by_visible_text("Option3")

dropdown_box = driver.find_element(By.ID,"autocomplete").send_keys("us")


time.sleep(5)
all_elements = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/div")
# print(all_elements)
# print(len(all_elements))
for i in all_elements:
    if 'Australia' == i.text:
        print(i.text)
        i.click()


time.sleep(5)

driver.quit()