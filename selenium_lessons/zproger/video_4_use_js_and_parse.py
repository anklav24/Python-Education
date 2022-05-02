from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.headless = True


# Go to about:config in the browser
# browser.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

def main():
    browser = webdriver.Firefox(options=option)
    browser.get('https://nickfinder.com/name-for-website')

    generate_button = browser.find_element(By.CSS_SELECTOR, 'span.btn.btn-sc.btn-block')

    for _ in range(10):
        generate_button.click()
        sitename = browser.find_element(By.CSS_SELECTOR, '#some_random_variants_web_2 > div:nth-child(1)')
        print(sitename.text)

    js_function_return = browser.execute_script("return generateAnotherWebsiteNameVariants(this, 'web_1');")
    print()
    print('js_function_return')
    print(js_function_return)

    browser.quit()


if __name__ == '__main__':
    main()
