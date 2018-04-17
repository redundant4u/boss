#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

def main():
	texta = goondaeNotice()
	print(texta)
	#makeFile(text)

def goondaeNotice():
	url = requests.get("https://www.mma.go.kr/contents.do?mc=mma0000743")
	html = url.text
	soup = BeautifulSoup(html, "html.parser")
	src = soup.find_all("tr").text
	encode = src
	return encode

def makeFile(text):
	file = open("/var/www/html/notice/daegoon.txt", "w")
	file.write(text)
	file.close()

if __name__ == "__main__":
	main()
