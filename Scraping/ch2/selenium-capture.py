from selenium.webdriver import Firefox, FirefoxOptions

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

options = FirefoxOptions()
options.add_argument('-headless')

browser = Firefox(options=options)

browser.get(url)

browser.save_screenshot("website.png")

browser.quit()
