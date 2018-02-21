import os, os.path
import re
from collections import Counter

wanted = 'NCAA'
cnt = Counter()

print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

DIR = '/home/ryan/Desktop/CS432/Assignment3/html_complete/'
dirpath = '/home/david/Desktop/CS432/Assignment3/html_complete/'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

for file in os.listdir(DIR):
	if file.endswith(".txt"):
		print(file,file=open('html_text.txt','a'))
with open('html_text.txt') as f:
    text = f.read().splitlines()
for name in text:
	filename=DIR+name
	print(filename)

	if 'NCAA' in open(filename).read():
		print("true")
		words = re.findall('\w+',open(filename).read().lower())
		for word in words:
			if word in wanted:
				cnt[word] += 1
				print(cnt)



import glob

def word_frequency(fileobj, words):
    ct = Counter(dict((w, 0) for w in words))
    file_words = (word for line in fileobj for word in line.split())
    filtered_words = (word for word in file_words if word in words)
    return Counter(filtered_words)


def count_words_in_dir(dirpath, words, action=None):
    for filepath in glob.iglob(os.path.join(dirpath, '*.txt')):
        with open(filepath) as f:
            ct = word_frequency(f, words)
            if action:
                action(filepath, ct)


def print_summary(filepath, ct):
    words = sorted(ct.keys())
    counts = [str(ct[k]) for k in words]
    print('{0}\n{1}\n{2}\n\n'.format(
        filepath,
        ', '.join(words),
        ', '.join(counts)))


words = set(['basketball', 'NBA', 'NCAA'])
count_words_in_dir('./', words, action=print_summary)
