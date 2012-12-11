# -*- coding: utf-8 -*-
import pycurl
import cStringIO
import re
import urllib as ul


queries = ["gabinet weterynaryjny chrzypsko",
		   # "gabinet weterynaryjny bogdan cegiełka",
		   # "weterynarz wronki"
			]
pageUrl = "wet-chrzypsko.pl"
position = 0


def getPage(query):
	c.setopt(c.URL, 'http://google.com/search?q='+query)
	c.perform()
	return buf.getvalue()

def getUrl(text, start=0):
	query = text.replace(" ", "+")
	page  = 10*start
	return query+"&start="+str(page)

def getPositionFromPage(page):
	global position
	success = False
	url = getUrl(query, page)
	result = getPage(url)

	m=re.compile('<h3 class="r">(.*?)</h3>')
	r=m.findall(result)
	for a in r:
		position+=1
		if(a.find(pageUrl) > 0):
			success = True
			break

	myFile = open('result', 'w')
	myFile.write(result)
	myFile.close()

	return success


buf = cStringIO.StringIO()
c = pycurl.Curl()
c.setopt(c.WRITEFUNCTION, buf.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (compatible; pycurl; pl-PL)")

for query in queries:
	position = 0
	page     = 0
	war      = False

	while not war:
		war = getPositionFromPage(page)
		buf.reset()
		page += 1

	print query," ",position
