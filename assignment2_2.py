import requests

links = [link.rstrip('\n') for link in open('input.txt')]

#Goes through status codes and sorts them
for link in links:
    try:
        r = requests.head(link)
        print(r.status_code)

        if (r.status_code) >= 400:
                print(link, file=open("400.txt", "a",))

        elif(r.status_code) >= 300 and (r.status_code) <= 399:
                print(link, file=open("300.txt", 'a'))

        elif(r.status_code) == 200:
                print(link, file=open("200.txt", 'a'))

        else:
                print(link, file=open("unknown.txt", 'a'))

    except requests.ConnectionError:
        print(link, file=open("invalid.txt", "a",))
