from selenium import webdriver
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=8pSC6QgxFzI&t=593s")

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

# 스크롤을 2번 내리는 구문
#while True: # 끝까지 내릴때
for i in range(0,2): # 2번만 내리겠다.
    # 스크롤을 내리고
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    time.sleep(1.5) # 댓글이 모두 로딩될때까지 기다리기 위해 1.5초 대기

    # 내린 상태의 높이를 new_height로 정의
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    # 내린 상태의 높이가 마지막 높이와 같다면 정지.
    if new_height == last_height: 
        break

    # 내린 상태의 높이 값 new_height를 마지막 높이로 재정의
    last_height = new_height

time.sleep(3)

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

#div중에 id가 header-author인걸 찾고 id가 autor-text인걸 찾고, span부분
id_list = soup.select("#author-text > span")
content_list = soup.select("#content-text")

# 크롤링한 유튜브 영상의 작성자와 내용을 csv파일로 저장
import pandas as pd

id_list_zip = []
content_list_zip = []

for i in range(0, len(id_list)):
    id_list_zip.append(str(id_list[i].text).strip())
    content_list_zip.append(content_list[i].text)

sdict = {"작성자": id_list_zip,
         "댓글": content_list_zip
         }

you_tube = pd.DataFrame(sdict)
you_tube.to_csv("youtube_result2.csv")

# print(content_list)

# for i in id_list:
#     # print(type(i)) # bs4.element.Tag
#     print(str(i.text).strip()) # i는 bs4의 객체이기 때문에 text 내장변수가 있다.

                        #yt-formatted-string 요소 중에 id가 content-text인것들 찾기
# comment_list = soup.select("yt-formatted-string#content-text")

# print(comment_list)