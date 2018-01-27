import sys
from bs4 import BeautifulSoup
import urllib.request
import requests
import re
if len(sys.argv) == 2:
	url =sys.argv[1]

else:
	print("Not enough arguments. Please retry.")
	sys.exit()

website = urllib.request.urlopen(url)

beauty = BeautifulSoup(website, "html.parser")

link_array = []

for link in beauty.findAll('a', attrs={'href': re.compile("^http")}):
	link_array.append(link.get('href'))

print("\nTotal URL's is ", len(link_array),"\n")
print(*link_array,sep='\n')

print("\n")

pdf_array = [s for s in link_array if ".pdf" in s]
print("The number of links which lead to .pdf files is: ",len(pdf_array),"\n")

print(*pdf_array,sep='\n')

print("\n")

for index, newurl in enumerate(pdf_array):
	response = requests.get(newurl)
	print(newurl, "is ", response.headers['content-length'], "bytes long")
