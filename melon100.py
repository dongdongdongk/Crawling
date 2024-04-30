import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

lst = lst50 + lst100

for rank, i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 > a")
    print(f"{rank} : {title.text}")
    print(singer.text)
    print("")