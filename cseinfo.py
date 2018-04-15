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
	fileInit()
	for noticeNumber in soup.find_all("td", class_="_artclTdNum"):
		startNumber = isNumber(noticeNumber.text)
		#print(locationNumber)
		if(startNumber):
			src = soup.find_all("tr")
			for i in range(locationNumber + 1, 16):
				title = src[i].find_all("td")[1].text
				date = src[i].find_all("td")[3].text
				processString(title, date)
				#rint(fixedTitle)
			break
		else:
			locationNumber += 1
	fileEnd()

def isNumber(number):
	try:
		int(number)
		return number
	except ValueError:
		return False

def fileInit():
	file = open("3.txt", "w")
	file.write("<?php\n\t$info = array (\n\t\t'notice' =>\n\t\tarray (\n\t\t\t")

def fileEnd():
	file = open("3.txt", "a")
	file.write("\n\t\t),\n\t);\n\t$array = json_encode($info);\n\techo $array;\n?>")

def processString(string, date):
	fixedTitle = string.replace("새글", "")
	fixedTitle2 = fixedTitle.strip()
	print(fixedTitle2)
	file = open("3.txt", "a")
	file.write("array (\n\t\t\t\t'title' => '" + fixedTitle2 + "',\n\t\t\t\t'date' => '")
	file.write(date + "',\n\t\t\t),\n\t\t\t")

if __name__ == "__main__":
	main()