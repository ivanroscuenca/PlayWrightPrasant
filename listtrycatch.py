from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')
        # Store multiple elements using list
        # elements = page.query_selector_all('b')
        # using a bad query to force try except and finally
        elements = page.query_selector('d//[@sf="werf"]').click()
        print(len(elements))
        for element in elements:
            print(element.text_content())
    except Exception as e:
        print(str(e))
    finally:
        print('execute')



