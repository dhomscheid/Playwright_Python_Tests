#tutorial: https://www.youtube.com/watch?v=E4wU8y7r1Uc
# changed links since side layout changed

#pip install pytest-playwright
#playwright install
#pip install rich

from playwright.sync_api import sync_playwright, Playwright
from rich import print
import json


def run(playwright: Playwright):
    start_url = "https://www.bhphotovideo.com/c/buy/SLR-Camera-Lenses/ci/274/N/4288584247"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort()) #block loading of pictures
    page.goto(start_url)
    i = 0
    while True:
        for link in page.locator("a[data-selenium='miniProductPageProductNameLink']").all(): #miniProductPageDetailsGridViewNameLink in video is now different
        #for link in page.locator("a[data-selenium='miniProductPageProductNameLink']").all()[:4]: #Only first few to test PageNext click 
            i += 1            
            p = browser.new_page(base_url="https://www.bhphotovideo.com/")
            p.route("**/*.{png,jpg,jpeg}", lambda route: route.abort()) #block loading of pictures
            url = link.get_attribute("href")
            if url is not None: 
                p.goto(url)
            else:
                p.close()

            data = p.locator("script[type='application/ld+json']").text_content()
            json_data = json.loads(data) #since data is a json string, put strvar into json var
            #print(json_data) #show data in json format, nicely formatted in console because of "rich"
            print(json_data["name"]) #Only show name

            p.close()

        totalItems = page.locator("span.pagination_e5tULaWwyv").text_content().split(" ")[0] #titleNumberingPagination #diffeerent solution than in video, there is only total number displayed. compar with i counter instead
        print(totalItems)

        if i >= int(totalItems):
            print("No more pages")
            break
        else:
            #data-selenium="listingPagingPageNext" #next button on end of page
            page.locator("a[data-selenium='listingPagingPageNext']").click()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)