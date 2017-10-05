import httplib2,time
from BeautifulSoup import BeautifulSoup, SoupStrainer

global start_link
start_link = 'https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=a' #Set Starting Link
links_list = ['https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=a']
num = 0

#Have program check for how many links are on the page
database_size = 500000 #how many links the database will contain
newlink = ''
f = open('database', 'w')

#Creates Initial Database \/ \/ \/
start = time.time()

while num <= database_size:     #Change to for x in links

    http = httplib2.Http()

    status, response = http.request(links_list[0])  # Make an HTTP request

    links_list = []

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if link['href'].startswith('/wiki/'): #Only will print the links that start with '/wiki/'
                #print link['href']
                #Add functionality to go to next page
                f.write('https://en.wikipedia.org' + link['href']+' \n')
                num += 1
                print num
            if link['href'].startswith('/w/index.php?title=Special:AllPages'):
                links_list.append('https://en.wikipedia.org' + link['href'])
                print links_list[0]




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