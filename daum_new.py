import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

url = "https://news.daum.net/"

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

item_issue = soup.select(".item_issue")

for item in item_issue:
    # press = item.select("thumb_g")[1]["alt"]

    press = item.select_one(".logo_cp > img")["alt"] # 언론사 

    category = item.select_one(".txt_category").text # 카테고리

    link_txt = item.select_one(".link_txt")
    link = link_txt['href']
    txt = link_txt.text.strip()

    print(f"{press} - {category}")
    print(f"{txt} : {link}")
    print("")