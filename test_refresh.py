#In Terminal
#pip install pytest-playwright
#playwright install

#Create an Exe File
#pip install pyinstaller
#create exe command: pyinstaller test_refresh.py --onefile --windowed

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto('http://localhost:8080/BC230/') #http://localhost:8080/BC230/ #https://workspace.google.com/marketplace/search/word
    
    i = 0
    while i < 10:
        page.keyboard.press('F5',delay=1000)
        page.reload()
        i += 1