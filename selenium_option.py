from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 사용자 에이전트(User-Agent) 설정
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# 사용자 데이터 디렉토리 경로 설정
user_data = r"F:\2024WebProject\webData\userData" # 유저 데이터 변수 추가 

# Chrome 옵션 설정
options = Options()

# 사용자 데이터 디렉토리 설정
options.add_argument(f"user-data-dir={user_data}")

# 자동화 방지를 위한 옵션 설정
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# WebDriver를 종료해도 브라우저가 종료되지 않도록 설정
options.add_experimental_option("detach", True)

# 브라우저 창을 최대 크기로 시작하도록 설정
options.add_argument("--start-maximized")
# 옵션 추가: 전체화면으로 시작 또는 특정 크기의 창으로 시작할 수 있음
# options.add_argument("--start-fullscreen")
# options.add_argument("window-size=500,500")

# 사용자 에이전트(User-Agent) 설정
options.add_argument(f"user-agent={user_agent}")

# 추가적인 옵션들
# options.add_argument("--headless") # headless 모드로 실행 (화면이 보이지 않음)
# options.add_argument("--disable-gpu") # GPU 사용 비활성화
# 예전에는 무조건 사용했지만, 현재는 크롬이 GPU를 사용하는 데에 문제가 없다면 필요하지 않을 수 있음

# WebDriver 생성 (Chrome을 사용)
driver = webdriver.Chrome(options=options)

# 접속할 URL 설정
url = "https://naver.com"

# 지정한 URL로 이동
driver.get(url)
