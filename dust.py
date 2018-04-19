#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup
from datetime import datetime

def main():
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
	url = requests.get("https://search.naver.com/search.naver?query=%EB%B6%80%EC%82%B0+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80", headers = headers)
	html = url.text
	soup = BeautifulSoup(html, "html.parser")
	src = soup.find_all("div", class_="detail_info lv5")
	AM_info = src[0].find_all("dl")[0]
	PM_info = src[1].find_all("dl")[0]

	print(datetime.today().strftime("%Y/%m/%d"))
	print(AM_info.text)
	print(PM_info.text)

if __name__ == '__main__':
	main()