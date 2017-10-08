import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

start = time.time()
fileLen = []
steps = ['']
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

    f.write('<' + str(i) + '> ' + '<' + str(linkNum) + '>' + ' ')
    fileLen.append('another one')
    #f.write(str(linkNum) + ' \n')
    #print pageLinks
    print len(fileLen)

    while True:  # main loop for going between wiki articles/
        x = 0
        http = httplib2.Http()
        status, response = http.request(i)
        steps = []
        for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
            if link.has_key('href'):
                if link['href'] != '/wiki/Wikipedia:Protection_policy#semi' and link['href'].startswith('#') == False and link['href'].startswith('/wiki/Wikipedia:') == False:
                    wikilink = 'https://en.wikipedia.org' + link['href']
                    print 'https://en.wikipedia.org' + link['href']
                    i = 'https://en.wikipedia.org' + link['href']
                    print steps
                    if i in steps == True:
                        print 'Im stuck in a loop!'
                        break
                    steps.append(i)
                    f.write(i + ' \n')
                    break

end = time.time()

totalTime = end - start

print 'Finished in ' + str(totalTime) + ' seconds'

f.close()
