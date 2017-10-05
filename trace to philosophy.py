import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

f = open('database.txt','r+')
links = f.readlines()

page_links = []

http = httplib2.Http()

for x in range(len(links)):
    links[x] = links[x][:-2]

for x in range(len(links)):
    print links[x]
    status, response = http.request(links[10])

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if link['href'].startswith('/wiki/'):
                page_links.append(link['href'])
    print page_links[10]