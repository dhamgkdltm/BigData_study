from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver.exe")

url = "https://www.naver.com"
driver.get(url)

driver.find_element(By.CSS_SELECTOR,'#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(8) > a').click()

time.sleep(5)

driver.find_element(By.CSS_SELECT,'#menu > li:nth-child(3) > a').click()

time.sleep(200)