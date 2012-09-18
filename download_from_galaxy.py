import BeautifulSoup as bs
import os
from cgi import escape
import httplib2
from optparse import OptionParser
import urllib
from urlparse import urlparse

def download(url, ext, baseUrl):

    http = httplib2.Http()

    status, page = http.request(url)

    soup = bs.BeautifulSoup(page)


    for a in soup('a'):
        if a.has_key('href'):
           if ext  == a['href'].split('.')[-1]:
               urlObj = urlparse(a['href'])
               if baseUrl is None:
                   finalUrl = 'wget %s%s'%tuple([urlObj.netloc, (urllib.quote(urlObj.path))]) 
               else:
                   finalUrl = 'wget %s%s'%tuple([baseUrl,(urllib.quote(urlObj.path))]) 
               print finalUrl
               os.system(finalUrl)


def parse_args():
    opt = OptionParser()
    opt.add_option('-u', '--url', dest = 'url', help = "Url to download from", metavar='URL')
    opt.add_option('-e', '--ext', dest = 'ext', help = 'File Name extension. ex., zip, mp3 etc', metavar='EXT')
    opt.add_option('-b', '--baseUrl', dest = 'baseUrl', help = 'Base url to start from. All download links in galaxy are relative urls', metavar='BASEURL')
    return opt.parse_args()

if __name__ == '__main__':

    (options, args) = parse_args()
    download(options.url, options.ext, options.baseUrl)
