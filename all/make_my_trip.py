from playwright.sync_api import sync_playwright
import time



with sync_playwright() as babuli:
    browser = babuli.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("https://www.makemytrip.com/")

    date_click = page.locator("//div[@class='flt_fsw_inputBox dates inactiveWidget ']")
    date_click.click()

    time.sleep(5)

    today = "//div[@class='DayPicker-Day DayPicker-Day--today']"
    next_two_days_date = page.locator(today+"/following-sibling::div[2]/div/p[1]")
    next_two_days_price = page.locator(today+"/following-sibling::div[2]/div/p[2]")

    print(next_two_days_date.text_content())

    print(next_two_days_price.text_content())


    browser.close()
