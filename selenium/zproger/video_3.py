import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

site = 'http://local.dev.elschool'
user_login = 'Administrator'
user_password = 'password'


def login(site, user_login, user_password):
    browser.get(site)
    login_button = browser.find_element(By.CSS_SELECTOR, '.btn-login')
    login_input = browser.find_element(By.CSS_SELECTOR, 'input[id="login_email"]')
    login_password = browser.find_element(By.CSS_SELECTOR, 'input[id="login_password"]')

    login_input.send_keys(user_login)
    login_password.send_keys(user_password)
    login_button.click()


class DeskSidebar:
    @staticmethod
    def click(href):
        browser.find_element(By.CSS_SELECTOR, f'a.desk-sidebar-item[href*="{href}"]')


def scroll(direction, count):
    html = browser.find_element(By.TAG_NAME, 'html')
    for _ in range(count):
        html.send_keys(direction)


def click_all_lists():
    lists = browser.find_elements(By.CSS_SELECTOR, '.link-item.ellipsis')
    for index, list in enumerate(lists):
        list.click()
        browser.save_screenshot(f'screenshots/{site.split("//")[-1]}_{index}.png')
        browser.back()


def main():
    login(site, user_login, user_password)

    desk_side_bar = DeskSidebar()
    desk_side_bar.click('журнал')
    time.sleep(1)
    click_all_lists()

    browser.quit()


if __name__ == '__main__':
    main()
