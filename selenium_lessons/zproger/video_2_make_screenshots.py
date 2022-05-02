from selenium import webdriver

browser = webdriver.Firefox()
sites = 'http://local.dev.elschool', 'https://google.com'

for site in sites:
    browser.get(site)
    browser.save_screenshot(f'screenshots/{site.split("//")[-1]}.png')
    browser.refresh()

browser.quit()
