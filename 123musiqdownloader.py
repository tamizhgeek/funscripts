import os
from BeautifulSoup import BeautifulSoup as bp
from BeautifulSoup import SoupStrainer
import urllib2

def download(page_name):
    print "http://123musiq.com/"+str(page_name)
    page = urllib2.urlopen("http://123musiq.com/"+str(page_name)).read()
    soup = bp(page)
    try:

        links = soup.findAll('a')
    except:
        links = soup.SoupStrainer('a')
    mp3 = []
    
    for li in links:
        if li['href'].endswith('.mp3'):
            mp3.append(li['href'])

    for a in mp3:
        os.system("wget http://123musiq.com/"+a)


if __name__ == "__main__":
    
    page_name = raw_input("enter page name with .htm extension: ")
    print page_name
    download(page_name)
    
