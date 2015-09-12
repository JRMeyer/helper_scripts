from bs4 import BeautifulSoup
import urllib
import sys

seedURL = 'http://'+sys.argv[1]

def stripLinksFromPage(myURL, seedURL):
    potentialLinks=[]
    r = urllib.urlopen(myURL).read()
    soup = BeautifulSoup(r)
    for link in soup.find_all('a'):
        if link.get('href').endswith('html'):
            if link.get('href').startswith(seedURL):
                potentialLinks.append(link['href'])
            else:
                potentialLinks.append(seedURL+link['href'])
    return potentialLinks

potentialLinks = stripLinksFromPage(seedURL,seedURL)

print len(potentialLinks)
