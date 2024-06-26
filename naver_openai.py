from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import requests

options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

options.add_argument("--start-maximized")

options.add_experimental_option("detach", True)

options.add_argument(f"user-agent={user_agent}")

options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동중 메세지 없에기 

driver = webdriver.Chrome(options=options)

keyword = input("검색할 제품을 입력하세요 : ")

url = f"https://search.shopping.naver.com/search/all?query={keyword}"


driver.get(url)
time.sleep(3)

for i in range(3):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

base_divs = soup.select("[class^=product_item]") # 원래 클래스 이름은 .product_item__MDtDF 이지만 뒤에 __ 이후 부터는 알아보기 힘들고 변경되는 경향이 있다 이때문에 product_item 으로 시작하는 클래스를 가져오란것 


main_text_list = [] # 하나로 합친 내용을 넣을 리스트

for num, base_div in enumerate(base_divs,1):
    title = base_div.select_one("[class^=product_title]")
    price = base_div.select_one("[class^=product_price]")
    detail_box_div = base_div.select_one("[class^=product_detail_box]")
    ad_button = base_div.select_one("[class^=ad_ad_stk]")

    if ad_button:
        continue
    
    # print(num)
    title_text = title.text
    price_text = price.get_text(" ")
    # print(title_text)
    # print(price_text)
   
    prod_text = f"{title_text} | {price_text}"
    
    if detail_box_div:
        detail_box_text = detail_box_div.get_text(" ")
        prod_text += f"\n{detail_box_text}"
        # print(detail_box_text)
    print(prod_text)

    main_text_list.append(prod_text)


