import os
from BeautifulSoup import BeautifulSoup as bp
import urllib2

def download(self, page_name = None):
    
    page = urllib2.urlopen(page_name).read()
    
    soup = bp(page)
    links = soup.findAll('a')
    
    mp3 = []
    
    for li in links:
        if li['href'].endswith('.mp3'):
            mp3.append(li['href'])

    for a in mp3:
        os.system("wget http://123musiq.com/"+a)


if __name__ == "__main__":
    
    download(page_name)

