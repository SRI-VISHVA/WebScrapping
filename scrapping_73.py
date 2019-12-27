from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import timeit

url = "https://www.investing.com/equities/trending-stocks"
driver = webdriver.Chrome(r"C:\Program Files\chromedriver.exe")
driver.get(url)
# x, stockPopularityData
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
print(soup)
a = list(soup.find_all("a", {"class": "bold block"}))
for i in a:
    a3 = list(str(i).split('>'))
    a4 = a3[1].split('<')
    print(str(a4[0]))
a = list(soup.find_all('script'))
# print(a)
b = str(a[43])
# Stock Popularity Data
print("Stock Popularity Data")
a1 = re.findall(r"stockPopularityData = .*;", b)
str = a1[0].replace(';', '')
str = str.split('=')
str1 = str[1].lstrip()
str3 = eval(str1)
for value1 in str3.values():
    for key, values in value1.items():
        print(key, values)
# Sector Popularity Data
print("Sector Popularity Data")
a3 = re.findall(r"sectorPopularityData = .*;", b)
str = a3[0].replace(';', '')
str = str.split('=')
str1 = str[1].lstrip()
str3 = eval(str1)
for value1 in str3.values():
    for key, values in value1.items():
        print(key, values)
# Trending Stock Quota by Price
print(soup.find_all('table', class_='genTbl closedTbl elpTbl elp20 crossRatesTbl'))
# Trending Stock Quota by Performance
python_button = driver.find_elements_by_xpath(xpath=r"/html/body/div[5]/section/div[7]/div/div[7]/div/a[2]")[0]
python_button.click()
# x, stockPopularityData
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
# print(soup)
print(soup.find_all('table', class_='genTbl openTbl recentQuotesSideBlockTbl collapsedTbl elpTbl elp30'))
# Trending Stock Quota by Technical
python_button = driver.find_elements_by_xpath(xpath=r"/html/body/div[5]/section/div[7]/div/div[7]/div/a[3]")[0]
python_button.click()
# x, stockPopularityData
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
print(soup)
