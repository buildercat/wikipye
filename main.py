import httplib2,timeit
from BeautifulSoup import BeautifulSoup, SoupStrainer

start_link = 'https://en.wikipedia.org/wiki/Special:AllPages/' #Set Starting Link

num = 0

#Have program check for how many links are on the page
links = 26

f = open('database', 'w')

#Creates Initial Database \/ \/ \/
start = timeit.timeit()
while num <= links:     #Change to for x in links

    http = httplib2.Http()

    for link in range(links):

        letter = chr(ord('A') + link)
        print (letter)

        status, response = http.request(start_link + letter)  # Make an HTTP request

        for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
            if link.has_key('href'):
                if link['href'].startswith('/wiki/'): #Only will print the links that start with '/wiki/'
                    print link['href']
                    #Add functionality to go to next page
                    f.write(link['href']+' \n')



    if letter == 'Z':
        f.close()
        break

end = timeit.timeit()  # Stop Timer

print end - start

f = open('database','r')
links_list = f.readlines()

for link in links_list:
    #status, response = http.request('https://en.wikipedia.org' + link)
    'https://en.wikipedia.org' + link

print links_list

    #Find first link on wiki page


    #Make an HTTP request to first link

    #Repeat until URL for Philosophy wikipedia page is reached


    #Input into database Wikipedia page name, how many steps it took to get to the philosophy wikipedia page, and how long it took`

    #Go back to beginning

