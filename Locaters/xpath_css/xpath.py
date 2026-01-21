from playwright.sync_api import sync_playwright
import time

with sync_playwright() as babuli:
    browser = babuli.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/Locaters/xpath_css/xpath_prac.html")


    time.sleep(5)

    browser.close()