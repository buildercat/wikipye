import httplib2,timeit
from BeautifulSoup import BeautifulSoup, SoupStrainer

start_link = 'https://en.wikipedia.org/wiki/Special:AllPages/' #Set Starting Link

num = 0

#Have program check for how many links are on the page
links = 26
while True:     #Change to for loop

    http = httplib2.Http()

    for link in range(links):
        start = timeit.timeit()  # Start Timer

        letter = chr(ord('A') + link)
        print (letter)

        status, response = http.request(start_link + letter)  # Make an HTTP request

        for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
            if link.has_key('href'):
                print link['href']

        end = timeit.timeit()  # Stop Timer
        print (end - start)




    #Find first link on wiki page


    #Make an HTTP request to first link

    #Repeat until URL for Philosophy wikipedia page is reached




    f = open('database','w+')
    #Input into database Wikipedia page name, how many steps it took to get to the philosophy wikipedia page, and how long it took`

    #Go back to beginning