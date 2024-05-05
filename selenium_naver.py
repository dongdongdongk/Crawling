from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

driver.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".spnew2.ico_nav_news").click()
time.sleep(3)

# driver.find_element(By.XPATH, '//a[contains(text(), "뉴스")]').click()

time.sleep(2)

driver.find_element(By.NAME, "query").clear()
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys("에스파")
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
time.sleep(2)

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".news_area")

for rank, item in enumerate(items,1):
    name = item.select_one(".info.press")
    title = item.select_one(".news_tit")

    print(f"<<{rank}>>")
    print(name.text)
    print(title.text)
    print("")

# driver.save_screenshot(r'F:\2024WebProject\Crawling\img\screenshot.png')
