# -*- coding: utf-8 -*-
import csv
import datetime

class File:

    def saveToFile(self, positions, name="positions.csv"):
        today = datetime.date.today()
        writer = csv.writer(open(name, 'a'))
        for query, position in positions.items():
            writer.writerow([today, query, position])

    def getFromFile(self, name="positions.csv"):
        file = csv.reader(open(name, "r", encoding='utf-8'))
        positions = []
        for data in file:
            positions.append([data[0].decode('utf8'), data[1].decode('utf8'), data[2].decode('utf8')])

        return positions