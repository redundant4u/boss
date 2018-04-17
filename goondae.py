#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

def main():
	goondaeNotice()

def goondaeNotice():
	url = requests.get("https://www.mma.go.kr/contents.do?mc=mma0000743")
	html = url.text
	soup = BeautifulSoup(html, "html.parser")
	src = soup.find_all("tr")
	
	print(src)

if __name__ == "__main__":
	main()