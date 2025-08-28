from playwright.sync_api import \
    sync_playwright  # Import Playwright's synchronous API

with sync_playwright() as p:  # Launch Playwright in a context manager
    browser = p.chromium.launch(
        headless=False)  # Launch Chromium browser in visible mode (headless=False)
    context = browser.new_context()  # Create a new browser context (like a separate browser profile)
    page = context.new_page()  # Open a new page (tab) in the context
    page.goto(
        'https://demo.automationtesting.in/Windows.html')  # Navigate to the demo website

    # Wait for the button with text "click" to appear and click it
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()

    page.wait_for_timeout(
        3000)  # Wait 3 seconds to allow new window/tab to open

    total_pages = context.pages  # Get a list of all open pages/tabs in the context
    print(len(total_pages))  # Print the total number of pages/tabs
    for i in total_pages:
        print(i)  # Print the object reference for each page/tab

    print(page.title())  # Print the title of the original page

    new_page = total_pages[1]  # Assume the second tab is the newly opened page
    new_page.bring_to_front()  # Bring the new page to the front (focus it)

    page.wait_for_timeout(3000)  # Wait another 3 seconds
    print(new_page.title())  # Print the title of the new page

    new_page.close()  # Close the new page/tab
