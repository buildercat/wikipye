import httplib2,timeit
#from BeautifulSoup import BeautifulSoup, SoupStrainer

start_link = 'https://en.wikipedia.org/wiki/Special:AllPages/' #Set Starting Link
while True:     #Change to for loop
    num = 0
    letter = 'A'

    http = httplib2.Http()

    for

    if num == 0:
        letter = 'A'
    if num == 1:
        letter = 'B'
    if num == 2:
        letter = 'C'
    if num == 3:
        letter = 'D'
    if num == 4:
        letter = 'E'
    if num == 5:
        letter = 'F'
    if num == 6:
        letter = 'G'
    if num == 7:
        letter = 'H'
    if num == 8:
        letter = 'I'
    if num == 9:
        letter = 'J'
    if num == 10:
        letter = 'K'
    if num == 11:
        letter = 'L'
    if num == 12:
        letter = 'M'
    if num == 13:
        letter = 'N'
    if num == 14:
        letter = 'O'
    if num == 15:
        letter = 'P'
    if num == 16:
        letter = 'Q'
    if num == 17:
        letter = 'R'
    if num == 18:
        letter = 'S'
    if num == 19:
        letter = 'T'
    if num == 20:
        letter = 'U'
    if num == 21:
        letter = 'V'
    if num == 22:
        letter = 'W'
    if num == 23:
        letter = 'X'
    if num == 24:
        letter = 'Y'
    if num == 25:
        letter = 'Z'

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