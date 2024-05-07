from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

# driver.find_element(By.XPATH, '//*[@title="검색어를 입력해 주세요."]').send_keys("블랙핑크", Keys.ENTER) # title 속성에 검색어를 입력해 주세요. 를 가진 요소 선택 바로 엔터하기
# time.sleep(2)

# # driver.find_element(By.XPATH, '//*[text()="뉴스"]').click() # 텍스트를 찾아서 뭔가를 할 정도는 알아야 한다 XPATH 
# driver.find_element(By.LINK_TEXT, "뉴스").click() # 텍스트가 "뉴스"인 하이퍼링크 요소를 찾는다. ( 주로 많이 사용 , 보통은 링크가 있는 텍스트를 찾아서 클릭을 많이 하기 때문 )
# time.sleep(2)

# driver.find_element(By.PARTIAL_LINK_TEXT, "블로").click() # 텍스트 중 일부만 포함해도 클릭하게 함 


navs = driver.find_elements(By.CSS_SELECTOR, ".link_service")


for num, i in enumerate(navs, 1):
    print(num)
    print(i.get_attribute("outerHTML"))
    print(i.text)
    print("")

    if i.text == "블로그":
        i.click()
        break
time.sleep(2)
