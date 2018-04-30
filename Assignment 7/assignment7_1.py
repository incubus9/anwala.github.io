
import urllib.request
from time import sleep
x = 0

for x in range (0, 100):
    try:
        url = 'https://www.blogger.com/next-blog?navBar=true&blogID=953024975153422094'
        response = urllib.request.urlopen(url)


        with open("blogs.txt", "a") as text_file:
            print(response.geturl(), file=text_file)
        sleep(2)
        
    except:
        x = x - 1
        pass
