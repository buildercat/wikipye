import httplib2,timeit
#from BeautifulSoup import BeautifulSoup, SoupStrainer

start_link = 'https://en.wikipedia.org/wiki/Special:AllPages/' #Set Starting Link

num = 0

#Have program check for how many links are on the page
links = 5
while True:     #Change to for loop

    http = httplib2.Http()

    for link in range(links):
        letter = chr(ord('A') + links)
        print (letter)

    start = timeit.timeit() #Start Timer

    status, response = http.request(start_link + letter) #Make an HTTP request

    #Find first link on wiki page

    #Make an HTTP request to first link

    #Repeat until URL for Philosophy wikipedia page is reached

    end = timeit.timeit() #Stop Timer

    f = open('database','w+')
    #Input into database Wikipedia page name, how many steps it took to get to the philosophy wikipedia page, and how long it took

    #Iterate to next starting link (AA - AB)

    #Go back to beginning