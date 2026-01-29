from playwright.sync_api import sync_playwright
import time



with sync_playwright() as babuli:
    browser = babuli.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/Locaters/xpath_css/xpath_prac.html")

    #1.using attribute (//tagname[@attribute='value'])
    username = page.locator("//input[@name='username']")
    username.fill("my name is khan")

    #2. using tagname (//tagname[text()='value'])
    login = page.locator("//button[text()='  Login   ']")
    login.click()
    print(login.text_content())

    #using conatins :- mostly doing the partial match. (//tagname[contains(@attribute/text(),'value')])
    click = page.locator("//button[contains(text(),'OTP ')]")
    click.click()
    print(click.text_content())


    #using normalize-space :- remove the unauthorized space from the text (//tagname[normalize-space(text()='value')]
    # // button[normalize - space() = 'Login']


    #start-with :- marching some first charcters, (//tagname[start-with(@attribute,'value')])
    # // a[starts -with(@ href, '/edit')]
    # hyperlink = page.locator("//a[starts-with(@href,'/edit')]").click()

    #and :- if both side condition should be True the locater hit on the DOM location
    #or :- atleast one them is correct.
    # //tagname[@attribute='value' and @attribute='value']
    # //tagname[@attribute='value' or @attribute='value']

    # // input[@ type = 'text' and @name ='username']
    # // input[ @ type = 'text' or @name='erfbre']

    #following-sibling " same hyrc up to down
    # // li[text() = ' Order 1003 '] / following - sibling::li[1]

    #precding :- down tp up
    # // li[text() = ' Order 1003 '] / preceding - sibling::li

    #parent :- if current posstion is in a child , then use parent
    # // li[text() = ' Order 1003 '] / parent::ul

    #child :- /  //section[@id='orders']/h2

    #ancestor
    # // td[text() = ' Bob '] / ancestor::tr / ancestor::tbody

    time.sleep(5)


    browser.close()

