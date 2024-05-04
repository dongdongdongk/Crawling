from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword

print(url)

driver = webdriver.Chrome()

driver.get(url)  # 페이지 로드를 기다리도록 수정
time.sleep(3) # 페이지를 불러오는데 대기 시간이 필요하기 떄문

# driver.execute_script("window.scrollTo(0,2000)") # 스크롤 약간 내리기
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 끝까지 스크롤 
    time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".view_wrap")

for rank, item in enumerate(items,1):
    name = item.select_one(".name")
    title = item.select_one(".title_link")

    print(f"<<{rank}>>")
    print(name.text)
    print(title.text)
    print("")
