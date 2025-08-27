from playwright.sync_api import sync_playwright

text_message = []   # list to store alert messages

# function to handle dialogs (alerts, confirms, prompts)
def handle_dialog(dialog):
    message = dialog.message              # capture text from alert
    text_message.append(message)          # store it in list
    dialog.accept()                       # click "OK" on the alert

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)   # open Chromium browser (visible)
    page = browser.new_page()                     # create new tab
    page.goto('https://demo.automationtesting.in/Alerts.html')  # go to demo alerts page

    # 1. Click the "Alert with OK & Cancel" tab (CancelTab)
    selected_button = page.wait_for_selector('//a[@href="#CancelTab"]')
    selected_button.click()

    page.wait_for_timeout(3000)   # wait 3 seconds (just for demo/visibility)

    # register event handler for alerts
    page.on('dialog', handle_dialog)

    # find the button that triggers alert in CancelTab
    click_button = page.wait_for_selector('//div[@id="CancelTab"]/button')
    click_button.click()  # click to open the alert

    page.wait_for_timeout(3000)   # wait 3 seconds (see alert handling in action)

    # print the text of the first captured alert
    print(text_message[0])
