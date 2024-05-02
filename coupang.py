import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

cookie = {"a" : "b"}

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색할 상품을 입력하세요 : ")

search_url = base_url + keyword

req = requests.get(search_url, timeout=5, headers=headers, cookies=cookie) #마냥 기다릴순 없기 때문에 5초 

# print(req.status_code) #응답 확인 

html = req.text

soup = BeautifulSoup(html, "html.parser")

# items = soup.select(".search-product") 이게 아니라

items = soup.select("[class=search-product]") # 이 방법을 사용해서 정확하게 어떤 클래스를 가져올지 정해줄 수 있다 ( 뒤에 다른 클래스가 붙지 않도록 )

rank = 1
for item in items:
     badge_rocket = item.select_one(".badge.rocket")
     if not badge_rocket:
          continue
     name = item.select_one(".name")
     price = item.select_one(".price-value")
     thumb = item.select_one(".search-product-wrap-img")
     link = item.select_one("a")['href']

     print(f"{rank}위")
     print(name.text)
     print(f"{price.text}원")
     print(f"https://coupang.com{link}")
     if thumb.get("data-img-src"):
        img_url = f"http:{thumb.get("data-img-src")}"
     else:
        img_url = f"http:{thumb["src"]}"
     print(img_url)
     print()

     img_req = requests.get(img_url)

     with open(f"{rank}.jpg","wb") as f:
         f.write(img_req.content)
     rank += 1