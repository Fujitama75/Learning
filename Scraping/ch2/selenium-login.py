from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

url_login = "https://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("ログインページ")

e = browser.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)

frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()
print("情報を入力してログインボタンを押しました。")

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin"))
)

a = browser.find_element_by_css_selector(".islogin a")
url_mypage = a.get_attribute('href')
print("マイページ=", url_mypage)

browser.get(url_mypage)

links = browser.find_elements_by_css_selector("#favlist li > a")

for a in links:
    href = a.get_attribute('href')
    title = a.text
    print("-", title, ">", href)
