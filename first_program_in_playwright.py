# 1.Role Locater :- get_by_role
# 2.Text locater :- get_by_text
# 3.Label Locater :- get_by_label
# 4.Placeholder locater :- get_by_placeholder
# 5.Alt Text Locater :- get_by_alt_text
# 6.Title Locater :- get_by_title
# 7.Test ID Locater :- get_by_test_id
# 8.CSS selector :- locater
# 9.Xpath :- locater


#Locater Priority Ordedr (Best to Worst)

# 1.get_by_test_id()
# 2.get_by_role()
# 3.get_by_label()
# 4.get_by_text()
# 5.get_by_placeholder()
# 6.locater(id,name)
# 7.locater(css)
# 8.Locater(xpath)
# 9.get_by_title()




#import playwright's synchrounous api
#sync_playwright() mangaes browser life cycle

from playwright.sync_api import sync_playwright
import time


#chromium - lunch
#headless=False --> browser visisbale
#with help of with ststament open context manager of playwright
with sync_playwright() as babuli:
    browser = babuli.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("https://www.facebook.com/login/")

    email = page.locator("#email").fill("babuli@gmail.com")
    password = page.locator("#pass").fill("babuli@123")

    submit = page.locator("#loginbutton").click()

    time.sleep(5)


    browser.close() # close the browser
























