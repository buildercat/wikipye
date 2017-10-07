import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer
f = open('database.txt','r+')
links = f.readlines()
f.close()

linkNum = []
pageLinks = []
for x in range(len(links)):
    links[x] = links[x][:-2]

print links

f = open('database.txt','w') #deletes old database file
f.close()
for x in links:
    pageLinks = []
    http = httplib2.Http()
    status, response = http.request(x)

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if link['href'].startswith('/wiki/'):
                pageLinks.append(link['href'])
    linkNum = len(pageLinks)
    print 'Number of links on page: ' + str(linkNum)
    f = open('database.txt','r+')
    f.write('<' + str(x) + '>' + ' ' + '<' + str(linkNum) + '>' + ' \n')
    f.close()
    #print pageLinks
