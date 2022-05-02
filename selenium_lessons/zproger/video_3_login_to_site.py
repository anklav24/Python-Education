import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class FrappeBrowser:
    def __init__(self, site, user_login, user_password, browser: webdriver):
        self.site = site
        self.user_login = user_login
        self.user_password = user_password
        self.browser = browser

    def login(self):
        self.browser.get(self.site)
        login_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-login')
        login_input = self.browser.find_element(By.CSS_SELECTOR, 'input[id="login_email"]')
        login_password = self.browser.find_element(By.CSS_SELECTOR, 'input[id="login_password"]')

        login_input.send_keys(self.user_login)
        login_password.send_keys(self.user_password)
        login_button.click()

    def scroll(self, direction, count):
        html = self.browser.find_element(By.TAG_NAME, 'html')
        for _ in range(count):
            html.send_keys(direction)

    def click_all_lists(self):
        lists = self.browser.find_elements(By.CSS_SELECTOR, '.link-item.ellipsis')
        for index, list in enumerate(lists):
            list.click()
            self.browser.save_screenshot(f'screenshots/{self.site.split("//")[-1]}_{index}.png')
            self.browser.back()


class DeskSidebar:
    def __init__(self, browser: webdriver):
        self.browser = browser

    def click(self, href):
        self.browser.find_element(By.CSS_SELECTOR, f'a.desk-sidebar-item[href*="{href}"]')


def main():
    options = webdriver.FirefoxOptions()
    options.headless = False
    browser = webdriver.Firefox(options=options)

    site = 'http://local.dev.elschool'
    user_login = 'Administrator'
    user_password = 'password'

    frappe_browser = FrappeBrowser(site, user_login, user_password, browser)
    frappe_browser.login()

    desk_side_bar = DeskSidebar(browser)
    desk_side_bar.click('журнал')
    time.sleep(1)
    frappe_browser.click_all_lists()
    time.sleep(1)
    date = browser.execute_script('return window.Date.now()')
    current_study_year = browser.execute_script('return frappe.boot.cur_study_year')
    print(f'{date = }')
    print(f'{current_study_year = }')

    browser.quit()


if __name__ == '__main__':
    main()
