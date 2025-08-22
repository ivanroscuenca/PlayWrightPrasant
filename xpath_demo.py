from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # xpath using attribute : '//tagname[@attributename = "value"]'
    # username = page.wait_for_selector('//input[@name="username"]')
    # username.type('Admin')
    #
    # password = page.wait_for_selector('//input[@name="password"]')
    # password.type('admin123')
    #
    # button = page.wait_for_selector('//button[@type="submit"]')
    # button.click()
    # page.wait_for_timeout(4000)

    # xpath using text : '//tagname[text()="value"]'
    forgot = page.wait_for_selector('//p[text()="Forgot your password? "]')
    forgot.click()
    page.wait_for_timeout(4000)

    # xpath using contains with :
    # attributes - //tagname[contains(@attribute, "value")]
    # //input[contains(@placeholder, "User")]
    # text - //tagname[contains(text(), "Forgot your")]
    # //label[contains(text(), "Username")]
    # dynamic - prasanth123, prasanth13454, prasanth987 / ivan123, prasant123, emma123
    # starts-with - //tagname[starts-with(@id, 'prasanth')]
    # ends-with - //tagname[ends-with(@id, '123')]

    # family
    # parent - //tagname[@id = "xy"]/parent::input[]
    # child - //tagname[@id = "xy"]/child::input[]
    # ancestor -
    # sibling - //td[text()="Microsoft"]/following-sibling::td[2]
