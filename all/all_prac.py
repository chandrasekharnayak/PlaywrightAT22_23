from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto(r"file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/all/webpage.html")
    #print the title in playwright
    print(page.title())

    #form of input box
    first_name = page.locator("#fname")
    first_name.fill("satya")

    page.fill("#lname",'Prakash')
    page.fill("#email","satya@test.com")

    #radio button
    page.locator("input[name='gender']").nth(1).click()
    # page.locator("//input[@name='gender'][2]").click()  # xpath

    page.fill("#mobile","9876543210")

    page.fill("input[type='date']","1977-03-01")
    time.sleep(5)

    browser.close()