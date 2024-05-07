from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")

options.add_argument("--start-maximized")

options.add_experimental_option("detach", True)

# options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

url = "https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(2)

if driver.current_url != url: # 현재 페이지가 url 이 아니라면 다시 접속하도록
    driver.get(url)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(1)

# 두 번째 더 보기 버튼 클릭
more_btns = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()

chart_list = driver.find_element(By.CSS_SELECTOR, "#_chartList")

items = chart_list.find_elements(By.CSS_SELECTOR, ".list_item")

print(len(items))

time.sleep(2)

# items = driver.find_elements(By.CSS_SELECTOR, ".list_item")

# for item in items[:]: # 반복문이 돌면서 삭제를 진행 할 경우에는 오류가 많다 그래서 복사를 해온 상태에서 반복문을 돌려 삭제하도록 한다
#     try:
#         ranking_num = item.find_element(By.CSS_SELECTOR, ".ranking_num")
#     except NoSuchElementException:
#         items.remove(items) # ranking_num 이 없는 아이템은 지운다 

# print(len(items))

action = ActionChains(driver)

action.move_to_element(items[90]).perform() # 원하는 엘리먼트로 이동하는 방벙 마지막에 perform() 을 붙여줘야 한다 



for rank, item in enumerate(items, 1):
    action.move_to_element(item).perform()

    name = item.find_element(By.CSS_SELECTOR, ".name.ellipsis")
    title = item.find_element(By.CSS_SELECTOR, ".title.ellipsis")

    thumb = item.find_element(By.CSS_SELECTOR, ".inner > span") # 정확한 접근
    thumb.click()
    time.sleep(1)
    album_url = driver.current_url
    driver.back()
    time.sleep(1)

    print(f"<<<{rank}>>>")
    print(name.text)
    print(title.text)
    print(f"album_url : {album_url}")

    time.sleep(1)

