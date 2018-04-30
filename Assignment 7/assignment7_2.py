import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests


fin = open("blogs.txt")
fout = open("blogsclean.txt", "w+")
delete_list = ['?expref=next-blog']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('blogs.txt', 'r') as istr:
    with open('blogsclean.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + 'feeds/posts/default'
            print(line, file=ostr)


