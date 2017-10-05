import httplib2,time,requests
from BeautifulSoup import BeautifulSoup, SoupStrainer

f = open('database.txt','r+')
links = f.readlines()

for x in range

for x in range(len(links)):
    print links[x]
    r = requests.get('https://en.wikipedia.org/wiki/A')
    print r.status_code