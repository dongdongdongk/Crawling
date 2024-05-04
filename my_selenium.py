from selenium import webdriver

url = "https://naver.com"

driver = webdriver.Chrome()

driver.get(url)


# 네이버 타이틀 가져오기 
title = driver.title

print(title)

# html 소스 500 자만 가져오기

html = driver.page_source

print(html[:500])