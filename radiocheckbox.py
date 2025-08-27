from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # 1. Select radio button
    radio_button = page.wait_for_selector('//input[@value="FeMale"]')
    #click or check button to select female(is the same)
    #radio_button.click()
    radio_button.check()
    if radio_button.is_checked():
        print('checked')
    else:
        print('not checked')

    # 2. checkbox selection
    checkbox = page.wait_for_selector('//input[@value="Cricket"]')
    checkbox.check()
    if checkbox.is_checked():
        print('checkbox selected')
    else:
        print('not checkbox selected')
    page.wait_for_timeout(3000)

