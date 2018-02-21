num_lines = 0

num_words = 0
num_chars = 0

listname = ('./html_complete/349ec66442a410163ddd3130f75e5c08.txt','./html_complete/2334985fd799ef1ca23751bb8756d6f8.txt','./html_complete/37b448a3130861a07bc81b3f77072b07.txt','./html_complete/d9aff423f6e55e87f26af8b426cbcc6c.txt','./html_complete/b7512b6982abbcd3385b59d9e0ea2e94.txt','./html_complete/d1cc32376d1f774ccf05767a31fafc66.txt','./html_complete/3ba1c07f0ff1c05ad0e3d2d469009614.txt','./html_complete/aabeda93399488822f80a811e7b1f781.txt','./html_complete/32bc42a50ba3917e76c041c9ec40bbb1.txt','./html_complete/13bb96482834bc8d6b365a08ef05661d.txt')

for name in listname:
	num_lines = 0
	num_words = 0
	num_chars = 0
	with open(name, 'r') as f:
		fname = f.read().splitlines()
		for line in fname:
			words = line.split()
			num_lines += 1
			num_words += len(words)
			num_chars += len(line)
		print(name)
print("Lines: ", num_lines,' Words: ',num_words,' Characters: ',num_chars)
