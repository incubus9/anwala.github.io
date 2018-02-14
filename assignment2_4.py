import json
import requests

with open('twitgone.txt') as data:
	text = data.read().splitlines()

for url in text:
	print('http://memgator.cs.odu.edu/timemap/json/', sep='', *url, file=open("gator.txt", "a"))

with open('gator.txt') as data:
	text = data.read().splitlines()

for ref,url in enumerate(text):
        req = requests.get(url)
        response = req.text
        inf = ref
        print('{0:04}'.format(inf),url)
        print('{0:04}'.format(inf),url,file=open('./data/memgator.txt','a'))
        filename = ''.join(str(x) for x in ("./data/memgator",'{0:04}'.format(inf),".txt"))
        print(response,file=open(filename,'w'))
