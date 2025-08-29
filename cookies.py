from playwright.sync_api import \
    sync_playwright  # Import Playwright's synchronous API

with sync_playwright() as p:  # Launch Playwright in a context manager
    browser = p.chromium.launch(
        headless=False)  # Launch Chromium browser in visible mode (headless=False)
    context = browser.new_context()  # Create a new browser context (like a separate browser profile)
    page = context.new_page()  # Open a new page (tab) in the context
    page.goto('https://www.redbus.in/')
    # give all cookies
    my_cookies = page.context.cookies()
    print(my_cookies)
    # clear all the cookies
    my_cookies.clear()
    # add new cookie
    new_cookie = {
        'name':'ivan',
        'udid':'13'
    }
    my_cookies.append(new_cookie)
    print(my_cookies)
    # take a screenhot
    page.screenshot(path='screenshot.png', full_page=True)


