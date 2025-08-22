from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # tagname[attribute = 'value']
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')

    password = page.wait_for_selector('input[name="password"]')
    password.type('admin123')

    button = page.wait_for_selector('button[type="submit"]')
    button.click()
    page.wait_for_timeout(4000)

