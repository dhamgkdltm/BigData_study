import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
result = requests.get(url) # <Response [200]> 반환

# print(result)

html = result.text  # html 내용 반환

# print(html)

soup = BeautifulSoup(html, "html.parser")
print(soup)