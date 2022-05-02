import pickle
import time

from selenium import webdriver

from video_3_login_to_site import FrappeBrowser


def open_on_the_second_monitor(browser):
    browser.set_window_position(1921, 1)
    browser.maximize_window()


def wait_stop_variable(browser: webdriver):
    print('Go to DevTools in the browser and create JS variable "stop = true"')
    stop = None
    while stop is not True:
        stop = browser.execute_script('return stop')
        print(f'{stop = }')
        time.sleep(1)


def save_cookies(browser):
    """Save cookies the file 'session'"""
    pickle.dump(browser.get_cookies(), open('session.pkl', 'wb'))
    print('Cookies have been saved into "session.pkl" file')


def load_cookies(browser):
    for cookie in pickle.load(open('session.pkl', 'rb')):
        print(f'{cookie = }')
        browser.add_cookie(cookie)


def open_browser_with_saved_cookies(browser, site):
    browser.get(site)
    load_cookies(browser)
    browser.refresh()
    print('Cookies have been loaded from "session.pkl" file')


def main():
    site = 'http://local.dev.elschool'
    user_login = 'Administrator'
    user_password = 'password'

    options = webdriver.FirefoxOptions()
    options.headless = False
    options.log.level = 'trace'
    options.add_argument('-devtools')  # Open dev tools by default
    browser = webdriver.Firefox(options=options)

    frappe_browser = FrappeBrowser(site, user_login, user_password, browser)

    open_on_the_second_monitor(browser)
    frappe_browser.login()
    wait_stop_variable(browser)
    save_cookies(browser)
    browser.refresh()
    browser.quit()

    browser = webdriver.Firefox(options=options)
    open_on_the_second_monitor(browser)
    open_browser_with_saved_cookies(browser, site)
    wait_stop_variable(browser)
    browser.quit()


if __name__ == '__main__':
    main()
