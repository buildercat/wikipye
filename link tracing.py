import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

start = time.time()
fileLen = []
f = open('database.txt','r+')
links = f.readlines()
f.close()

linkNum = []
pageLinks = []
for x in range(len(links)):
    links[x] = links[x][:-2]

print links

f = open('database.txt','w') #deletes old database file

for i in links:
    pageLinks = []
    http = httplib2.Http()
    status, response = http.request(i)

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if link['href'].startswith('/wiki/'):
                pageLinks.append(link['href'])
    linkNum = len(pageLinks)
    print 'Number of links on page: ' + str(linkNum)

    f.write('<' + str(i) + '> ' + '<' + str(linkNum) + '>' + ' \n')
    fileLen.append('another one')
    #f.write(str(linkNum) + ' \n')
    #print pageLinks
    print len(fileLen)
end = time.time()

totalTime = end - start

print 'Finished in ' + totalTime + ' seconds'

f.close()
