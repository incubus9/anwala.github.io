import csv
import math
import operator
from collections import Counter
import string

def euclideanDistance(P, Q):
	if( len(P) != len(Q) ):
		return -1
	sumOfSquares = 0
	for i in range(0, len(P)):
		sumOfSquares += (P[i] - Q[i]) * (P[i] - Q[i])
	return math.sqrt(sumOfSquares)



P = [33,1,19]

with open('data/u.user') as tsv:
	for line in csv.reader(tsv, delimiter="|"):
		if line[2] == "M":
			line[2] = '1'
		if line[2] == "F":
			line[2] = '2'
		if line[3] == "administrator":
			line[3] = '1'              
		if line[3] == "artist":
			line[3] = '2'
		if line[3] == "doctor":
			line[3] = 3
		if line[3] == "educator":
			line[3] = 4
		if line[3] == "engineer":
			line[3] = 5
		if line[3] == "entertainment":
			line[3] = 6
		if line[3] == "executive":
			line[3] = 7
		if line[3] == "healthcare":
			line[3] = 8
		if line[3] == "homemaker":
			line[3] = 9
		if line[3] == "lawyer":
			line[3] = 10
		if line[3] == "librarian":
			line[3] = 11
		if line[3] == "marketing":
			line[3] = 12
		if line[3] == "none":
			line[3] = 13
		if line[3] == "other":
			line[3] = 14
		if line[3] == "programmer":
			line[3] = 15
		if line[3] == "retired":
			line[3] = 16
		if line[3] == "salesman":
			line[3] = 17
		if line[3] == "scientist":
			line[3] = 18
		if line[3] == "student":
			line[3] = 19
		if line[3] == "technician":
			line[3] = 20
		if line[3] == "writer":
			line[3] = 21
		Q = [int(line[1]),int(line[2]),int(line[3])]
		print(line[0], euclideanDistance(P, Q),file=open('distance.txt','a'))

sample = open("distance.txt")
csv1 = csv.reader(sample, delimiter=' ')
sort = sorted(csv1, key=lambda x : (x[1]))
for eachline in sort:
    print(eachline)

