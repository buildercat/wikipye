import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

start = time.time()
fileLen = []
steps = []
f = open('database.txt','r+')
links = f.readlines()
f.close()

linkNum = []
pageLinks = []
for x in range(len(links)):
    links[x] = links[x][:-2]

print links
f = open('database.txt','w')

for i in links:
    f = open('database.txt', 'r+')  #deletes old database filepageLinks = []
    http = httplib2.Http()
    status, response = http.request(i)

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if link['href'].startswith('/wiki/'):
                pageLinks.append(link['href'])
    linkNum = len(pageLinks)
    print 'Number of links on page: ' + str(linkNum)

    f.write('<' + str(i) + '> ' + '<' + str(linkNum) + '>' + ' ' + '<')
    fileLen.append('another one')
    #f.write(str(linkNum) + ' \n')
    #print pageLinks
    print len(fileLen)

    http = httplib2.Http()

    try:
        while i != 'https://en.wikipedia.org/wiki/Philosophy':  # main loop for going between wiki articles/
            x = 0
            status, response = http.request(i)
            #steps = []
            for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
                if link.has_key('href'):
                    if link['href'] != '/wiki/Wikipedia:Protection_policy#semi' and link['href'].startswith('#') == False and link['href'].startswith('/wiki/Wikipedia:') == False and link['href'].startswith('/wiki/File:') == False: #Blacklist of links not to follow
                        wikilink = 'https://en.wikipedia.org' + link['href']
                        #print 'https://en.wikipedia.org' + link['href']
                        i = 'https://en.wikipedia.org' + link['href']
                        print steps1
                        if i in steps: #Loop for if it gets stuck in a loop
                            print "I'm stuck in a loop!"
                            f.write('True' + ' \n')
                            f.close()
                            raise StopIteration()
                            break
                        steps.append(i)
                        f.write(i + '   ')
                        break

    except StopIteration: #This will run after the while loop is ended
        pass
        end = time.time()
        print 'Completed in ' + str(end - start) + ' seconds'
        steps = []


end = time.time()

totalTime = end - start

print 'Finished in ' + str(totalTime) + ' seconds'

f.close()

#ADD LOOP TO DELAY IF httplib.ResponseNotReady() == TRUE