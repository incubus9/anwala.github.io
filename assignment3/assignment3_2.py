import boilerpipe
from boilerpipe.extract import Extractor
import os, os.path
import re


print(len([name for name in os.listdir('.') if os.path.isfile(name)]))


DIR ='/home/ryan/Desktop/CS432/Assignment3/html/'
DIR2 = '/home/ryan/Desktop/CS432/Assignment3/html_complete/'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

for file in os.listdir(DIR):
	if file.endswith(".html"):
		print(file,file=open('htmlcomp.txt','a'))
	
with open('htmlcomp.txt') as f:
    text = f.read().splitlines()
for file in text:
	try:
		filename=DIR+file
		x = open(filename)
		html = x.read()
		extractor = Extractor(extractor='ArticleExtractor', html=html)
		processed = extractor.getText()
		newfile = re.sub('html', 'txt', file)
		newfileloc = DIR2+newfile
		print(processed,file=open(newfileloc,'w'))
	except UnicodeDecodeError:
		print("Error.",file,file=open('Error.txt','a'))
	except Exception:
		print("No Text.",file,file=open('Notext.txt','a'))
