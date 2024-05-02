import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

sect_movie_chart = soup.select_one(".sect-movie-chart")

movie_chart = sect_movie_chart.select("li")

for rank, movie in enumerate(movie_chart, 1):
    title = movie.select_one(".title")
    score = movie.select_one(".score")
    ticketing = score.select_one(".percent")
    egg_gage = score.select_one(".egg-gage.small > .percent") # egg-gate 클래스 하위 .percent 클래스를 찾아 선택

    info = movie.select_one(".txt-info > strong").next_element # 그냥 개봉을 아예 가져오지 않게 해버림 next_element 를 사용해서 
    
    print(f"<<rank{rank}위>>")
    print(title.text)
    print(ticketing.get_text(" : "))
    print(egg_gage.text)
    print(f"{info.strip()}")
    print("")

# print(len(movie_chart))



