import os, os.path
import re


print(len([name for name in os.listdir('.') if os.path.isfile(name)]))


DIR ='/home/ryan/Desktop/CS432/Assignment3/html/'
DIR2 = '/home/ryan/Desktop/CS432/Assignment3/html_complete/'
print('html directory count: ',len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
print('processed directory count: ',len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))]))

file=open('twitgone.txt', 'r')
uri = file.read().split('\n')
file.close()

file=open('htmlcomp.txt', 'r')
html = file.read().split('\n')
file.close()

file=open('Notext.txt', 'r')
notext = file.read().split('\n')
file.close()

file=open('Error.txt', 'r')
error = file.read().split('\n')
file.close()

file=open('mincount.txt', 'r')
minwo = file.read().split('\n')
file.close()


print(len(uri))
print(len(html))
print(len(notext))
print(len(error))
print(len(minwo))
