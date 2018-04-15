#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

def main():
	cseNotice()

def cseNotice():
	locationNumber = 0
	url = requests.get("https://cse.pusan.ac.kr/cse/14651/subview.do")
	html = url.text
	soup = BeautifulSoup(html, "html.parser")
	#src = soup.find_all("td", class_="_artclTdNum")

	for noticeNumber in soup.find_all("td", class_="_artclTdNum"):
		startNumber = isNumber(noticeNumber.text)
		#print(locationNumber)
		if(startNumber):
			src = soup.find_all("tr")
			for i in range(locationNumber + 1, 16):
				title = src[i].find_all("td")[1].text
				print(title)
			break
		else:
			locationNumber += 1

	
def isNumber(number):
	try:
		int(number)
		return number
	except ValueError:
		return False

if __name__ == "__main__":
	main()