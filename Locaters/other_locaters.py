from playwright.sync_api import sync_playwright
import time

with sync_playwright() as babuli:
    browser = babuli.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/Locaters/other_locaters.html")


    #get by role (tagname, text)
    '''submit = page.get_by_role("button",name="submit")
    submit.click()
    print(submit.text_content())
    time.sleep(3)'''

    #get by label
    '''username = page.get_by_label("Username")
    username.fill("admin")

    password = page.get_by_label("Password")
    password.fill("password")

    time.sleep(3)
    page.get_by_role("button",name ="Login" ).click()

    time.sleep(3)'''

    #get by text
    '''text1 = page.get_by_text("Welcome to Playwright automation practice").is_visible()
    print(text1)
    time.sleep(3)
    page.get_by_text(" Accept Terms and Conditions").click()
    time.sleep(3)'''

    #get by placeholder
    time.sleep(3)

    email = page.get_by_placeholder("Enter your email").fill("a@gmail.com")
    search = page.get_by_placeholder("Search here").fill("email")

    time.sleep(3)

    browser.close()