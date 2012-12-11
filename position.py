# -*- coding: utf-8 -*-
import pycurl
import cStringIO
import re

class Position:

	def __init__(self, queries, url):
		self.queries  = queries
		self.pageUrl  = url
		self.position = 0

		self.buf = cStringIO.StringIO()
		self.c = pycurl.Curl()
		self.c.setopt(self.c.WRITEFUNCTION, self.buf.write)
		self.c.setopt(pycurl.FOLLOWLOCATION, 1)
		self.c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (compatible; pycurl; pl-PL)")

	def getPage(self, query):
		self.c.setopt(self.c.URL, 'http://google.pl/search?q='+query)
		self.c.perform()
		return self.buf.getvalue()

	def getUrl(self, text, start=0):
		query = text.replace(" ", "+")
		page  = 10 * start
		return query+"&start="+str(page)

	def getPositionFromPage(self, query, page):
		success = False
		url = self.getUrl(query, page)
		result = self.getPage(url)

		m=re.compile('<h3 class="r">(.*?)</h3>')
		r=m.findall(result)
		for a in r:
			self.position += 1
			if(a.find(self.pageUrl) > 0):
				success = True
				break
				
		return success

	def run(self):
		positions = {}

		for query in self.queries:
			self.position = 0
			page          = 0
			war           = False

			while not war:
				war = self.getPositionFromPage(query, page)
				self.buf.reset()
				page += 1

			positions[query] = self.position

		return positions