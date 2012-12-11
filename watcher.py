#!/usr/bin/python
# -*- coding: utf-8 -*-
from position import Position
from file import File

queries = [
           "gabinet weterynaryjny chrzypsko",
		   "gabinet weterynaryjny bogdan cegiełka",
		   "weterynarz wronki"
	      ]
pageUrl = "wet-chrzypsko.pl"



#pos = Position(queries, pageUrl)
#actualPositions = pos.run()
file = File()
#file.saveToFile(actualPositions)
print file.getFromFile()

