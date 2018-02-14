import os
import json
import re
import fileinput
import sys
import time
from pprint import pprint
from collections import Counter

Path = "./data/"
filelist = os.listdir(Path)

for i in filelist:
	if i.startswith("memgator0") and i.endswith(".txt"):
		with open(Path + i, 'r') as infile:
			filename = Path + i
			searchlines = infile.readlines()
		for i, line in enumerate(searchlines):
			if "404 page not found" in line:
				print('This is a 404 file ', filename ,file=open('memgator404.txt','a'))
				print('This is a 404 file ', filename)
			else:
				print(filename, file=open('memgator.txt','a'))
				print(filename)


content = open('memgator.txt', 'r').readlines()
content_set = set(content)
cleandata = open('memgator.file', 'w')

for line in content_set:
	cleandata.write(line)


with open('memgator.file','r') as file_list:
	filename = file_list.read().splitlines()

	for ref,filename in enumerate(filename):

		with open(filename, 'r') as json_file:
			try:	
				json_data = json.load(json_file)
				print(len(json_data['mementos']['list']),file=open('histograph.data','a'))	
			except ValueError:
                                print("JSON object issue: ",filename, file=open('memojson_fail.txt', 'a'))
