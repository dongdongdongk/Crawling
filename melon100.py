import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

song_num_text = "javascript:melon.link.goAlbumDetail('11474894');"

# 빈 리스트 song_num을 생성합니다.
def get_song_nums(song_num_text):
    # song_num = []
    
    # # song_num_text의 각 문자에 대해 반복합니다.
    # for num in song_num_text:
    #     # 만약 문자가 숫자인지 확인합니다.
    #     if num.isdigit():
    #         # 숫자인 경우 song_num 리스트에 추가합니다.
    #         song_num.append(num)
    # # join() 함수는 문자열을 이어붙이는 역할
    # song_num="".join(song_num)

    # return song_num

    song_num = "".join([num for num in song_num_text if num.isdigit()])
    return song_num

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst = lst50 + lst100

# lst = soup.find_all(class_=["lst50","lst100"])

lst = soup.select(".lst50, .lst100")

for rank, i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a")
    
    singer = i.select_one(".ellipsis.rank02 > a")
    singer_link = get_song_nums(singer['href'])

    album = i.select_one(".ellipsis.rank03 > a")
    album_link = get_song_nums(album['href'])
    print(f"{rank} : {title.text}")
    print(f"{singer.text} : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"{album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}")
    print("")