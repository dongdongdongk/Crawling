from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

options = Options()

options.add_experimental_option("detach", True) # 바로 종료되지 않게 옵션 추가 

options.add_argument("--start-maximized") # 화면을 최대 크기로 시작
# options.add_argument("--start-fullscreen") # 화면을 전체화면으로 시작
# options.add_argument("window-size=500,500") # 화면을 500 500 으로

options.add_argument(f"user-agent={user_agent}") # user_agent 추가 

# options.add_argument("--headless") # headless 모드 
# options.add_argument("--disable-gpu") # 예전에는 무조건 같이 사용했지만 지금은 없어도 괜찮다 

options.add_argument("--mute-audio") # 음소거 모드 
options.add_argument("incognito") # 시크릿 모드 

options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동중 메세지 없에기 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸때없는 로그 없에기 

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)

print(driver.page_source[:1000])




