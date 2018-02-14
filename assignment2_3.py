import re
import requests

#clean the file of duplicates
unclean = open('200.txt', 'r').readlines()
clean_set = set(unclean)
clean = open('200nodup.txt', 'w')

for line in clean_set:
	clean.write(line)

#remove any twitter links
error = []
string = re.compile("twitter.com", re.IGNORECASE)

try:
	with open ('200nodup.txt', 'rt') as in_file:
		for linenum, line in enumerate(in_file):
			if string.search(line) != None:
				error.append((linenum, line.rstrip('\n')))
			else:
				print(line, file=open("twitrem.txt", 'a'))

except FileNotFoundError:
	print ("File Not Found")

for line in open('twitrem.txt'):
	line = line.rstrip()
	if line != '':
		print(line, file=open('twitgone.txt', 'a'))


#does a quick count of all the lines in the file
file=open('input.txt', 'r')
input_count = file.read().split('\n')
file.close()

file=open('200.txt', 'r')
found_count = file.read().split('\n')
file.close()

file=open('300.txt', 'r')
redir_count = file.read().split('\n')
file.close()

file=open('400.txt', 'r')
bad_count = file.read().split('\n')
file.close()

file=open('twitgone.txt', 'r')
clean_count = file.read().split('\n')
file.close()


print(len(input_count)-1, "is the original search history")
print(len(found_count)-1, "is the number with server code 200")
print(len(redir_count)-1, "is the number with server code 300")
print(len(bad_count)-1, "is the number with server code 400")
print(len(clean_count)-1, "is the number after cleaning data")


