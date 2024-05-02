import requests
from bs4 import BeautifulSoup

url = "https://www.ssg.com/event/eventMain.ssg"


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

evt_osmu_lst = soup.select_one(".evt_osmu_lst")

units  = evt_osmu_lst.select(".eo_link")

# print(len(units))

for unit in units:
    link = unit['href']
    if link.startswith("https"):
        print(link)
    else:
        print(f"https://www.ssg.con//{link}")

    eo_in = unit.select_one(".eo_in") # 텍스트전체 들어있는 가장 가까운 class

    text_list = eo_in.find_all(string=True) # 스트링 요소를 전부 찾음

    for text in text_list: # \n 이 들어있는데 이를 빼고 출력
        if text != "\n":
            print(text)
    print("")
