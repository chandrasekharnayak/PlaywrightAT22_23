from playwright.sync_api import sync_playwright
import time


with sync_playwright() as babuli:
    browser = babuli.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/wait/wait.html")

    text = page.locator("//h2[text()='Playwright Wait Demo']")
    print(text.text_content())

    # page.wait_for_timeout(36000) # hard wait from playwright

    # button = page.locator("#loginBtn")
    # button.click()
    # print(button.text_content())

    page.wait_for_selector("#loginBtn")
    page.click("#loginBtn")
    print(page.text_content("#loginBtn"))





    browser.close() # close the browser
#
#
#
#
#


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get(r"file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/wait/wait.html")
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# text = driver.find_element(By.XPATH,"//h2[text()='Playwright Wait Demo']").text
# print(text)
#
# buuton = driver.find_element(By.ID,"loginBtn")
# buuton.click()
# print(buuton.text)



# driver.quit()