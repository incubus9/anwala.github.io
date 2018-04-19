import csv
import math
import operator
import string
from collections import Counter
from math import sqrt
import re
import sys

def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    for (item, rating) in userRatings.items():
        for (similarity, item2) in itemMatch[item]:
            if item2 in userRatings:
                continue
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    rankings = [(score / totalSim[item], item) for (item, score) in
               scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

with open('/home/ryan/Desktop/CS432/Assignment6/data/u.data') as tsv:
	for line in csv.reader(tsv, delimiter="\t"):
		rate = int(line[2])
		movie = int(line[1])
		user = line[0]
		if user == '124':
			print(user, movie, rate,file=open('124.txt','a'))
		if user == '183':
			print(user, movie, rate,file=open('183.txt','a'))
		if user == '272':
			print(user, movie, rate,file=open('272.txt','a'))

sample = open("124.txt")
csv1 = csv.reader(sample, delimiter=' ')
sort = sorted(csv1, key=lambda x : (int(x[2]),int(x[1])))
with open("124movie.csv", 'wt') as f:
	writer = csv.writer(f)
	for eachline in sort:
		writer.writerow(eachline)
		print(eachline)

sample = open("183.txt")
csv1 = csv.reader(sample, delimiter=' ')
sort = sorted(csv1, key=lambda x : (int(x[2]),int(x[1])))
with open("183movie.csv", 'wt') as f:
	writer = csv.writer(f)
	for eachline in sort:
		writer.writerow(eachline)
		print(eachline)

sample = open("272.txt")
csv1 = csv.reader(sample, delimiter=' ')
sort = sorted(csv1, key=lambda x : (int(x[2]),int(x[1])))
with open("272movie.csv", 'wt') as f:
	writer = csv.writer(f)
	for eachline in sort:
		writer.writerow(eachline)
		print(eachline)


with open('/home/ryan/Desktop/CS432/Assignment6/data/u.item', encoding = "ISO-8859-1") as tsv:
	for line in csv.reader(tsv, delimiter="|"):
		with open('124movie.csv') as mvs:
			for line2 in csv.reader(mvs, delimiter=","):
				if line2[2] == '1':
					if line2[1] == line[0]:	
						print(line2[2],'&',line[1],file=open		('124movierank1.tsv','a'))	
				if line2[2] == '5':
					if line2[1] == line[0]:
						print(line2[2],'&',line[1],file=open('124movierank5.tsv','a'))

with open('/home/ryan/Desktop/CS432/Assignment6/data/u.item', encoding = "ISO-8859-1") as tsv:
	for line in csv.reader(tsv, delimiter="|"):
		with open('183movie.csv') as mvs:
			for line2 in csv.reader(mvs, delimiter=","):
				if line2[2] == '1':
					if line2[1] == line[0]:	
						print(line2[2],'&',line[1],file=open		('183movierank1.tsv','a'))	
				if line2[2] == '5':
					if line2[1] == line[0]:
						print(line2[2],'&',line[1],file=open('183movierank5.tsv','a'))

with open('/home/ryan/Desktop/CS432/Assignment6/data/u.item', encoding = "ISO-8859-1") as tsv:
	for line in csv.reader(tsv, delimiter="|"):
		with open('272movie.csv') as mvs:
			for line2 in csv.reader(mvs, delimiter=","):
				if line2[2] == '1':
					if line2[1] == line[0]:	
						print(line2[2],'&',line[1],file=open		('272movierank1.tsv','a'))	
				if line2[2] == '5':
					if line2[1] == line[0]:
						print(line2[2],'&',line[1],file=open('272movierank5.tsv','a'))
