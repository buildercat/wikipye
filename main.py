import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

global start_link
start_link = 'https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=%21' #Set Starting Link

num = 0

#Have program check for how many links are on the page
links = 26
newlink = ''
f = open('database', 'w')

#Creates Initial Database \/ \/ \/
start = time.time()

while num <= links:     #Change to for x in links

    http = httplib2.Http()

    status, response = http.request(start_link)  # Make an HTTP request

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if link['href'].startswith('/wiki/'): #Only will print the links that start with '/wiki/'
                print link['href']
                #Add functionality to go to next page
                f.write('https://en.wikipedia.org' + link['href']+' \n')
            if link['href'].startswith('/w/index.php?title=Special:AllPages'):
                print link['href']
                start_link = 'https://en.wikipedia.org' + link['href']




end = time.time()  # Stop Timer

print end - start

f = open('database','r')
links_list = f.readlines()

for link in links_list:
    #status, response = http.request('https://en.wikipedia.org' + link)
    print 'https://en.wikipedia.org' + link
    #print response

print links_list

    #Find first link on wiki page


    #Make an HTTP request to first link

    #Repeat until URL for Philosophy wikipedia page is reached


    #Input into database Wikipedia page name, how many steps it took to get to the philosophy wikipedia page, and how long it took`

    #Go back to beginning
