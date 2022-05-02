from selenium import webdriver
from selenium_stealth import stealth

from video_5_cookie_import_export import open_on_the_second_monitor


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.headless = False

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    site = 'https://mynickname.com/generate'
    # site = 'https://kontur.ru/market'
    # site = 'https://google.com'
    open_on_the_second_monitor(driver)
    driver.get(site)
    # nickname = driver.execute_script('return genName(document.forms[1])')
    date = driver.execute_script('return window.Date.now()')
    print(date)
    driver.quit()


if __name__ == '__main__':
    main()
