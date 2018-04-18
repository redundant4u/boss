#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

def main():
	text = goondaeNotice()
	#print(texta)
	makeFile(text)

def goondaeNotice():
	text = ""
	url = requests.get("https://www.mma.go.kr/contents.do?mc=mma0000743")
	html = url.text
	soup = BeautifulSoup(html, "html.parser")
	for info in soup.find_all("tr"):
		text += str(info);
	return text

def makeFile(text):
	text = str(text)
	file = open("/var/www/html/notice/daegoon.txt", "w")
	file.write(text)
	file.close()

if __name__ == "__main__":
	main()
