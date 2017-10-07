import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

f = open('database.txt','r+')
links = f.readlines()

new_link = ''

http = httplib2.Http()

for x in range(len(links)):
    links[x] = links[x][:-2]

def getlinks (url):
    status, response = http.request(url)

    y = 0

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            y += 1
            if y == 6:
                new_link = 'https://en.wikipedia.org' + link['href']
                print link['href']
                new_link = 'https://en.wikipedia.org' + link['href']
                break

for x in range(len(links)):
    print links[x]
    status, response = http.request('https://en.wikipedia.org' + links[x])
    page_links = []

    y = 0
'''
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            y += 1
            if y == 6:
                new_link = 'https://en.wikipedia.org' + link['href']
                print link['href']
                new_link = 'https://en.wikipedia.org' + link['href']
                break
'''