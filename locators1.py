from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/')

    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('test@gmail.com')

    buttonlogin = page.wait_for_selector('#enterimg')
    buttonlogin.click()
    page.wait_for_timeout(2000)



