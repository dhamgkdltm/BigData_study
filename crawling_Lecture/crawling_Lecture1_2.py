import requests
from bs4 import BeautifulSoup
url = "https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
response = requests.get(url)

# 200(성공): 서버가 요청을 제대로 처리했다는 뜻.
# 네이버 지식인에 파이썬을 검색한 url. 응답 코드가 200일 때, html을 받아와 soup 객체로 변환.
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # ul 태그 중 basic1 클래스를 가진 녀석을 뽑아오는 선택자
    ul = soup.select_one('ul.basic1') # '태그.클래스명'
    
    # ul 자식태그에는 li 태그가 10개
    # 각 li 태그 안에는 dl > dt > a 태그 안에 제목이 들어있다.
    # li > dl > dt > a 는 자식 선택자를 이용한 것
    titles = ul.select('li > dl > dt > a')
    # print(titles) # 리스트 형식으로 반환
    
    for title in titles:
      print(title.get_text())

else:
    print(response.status_code)