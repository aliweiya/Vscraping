#now we ended the day 1 ,
#just a happy start
#next , let's think about:
#a spider scraping in the net all day long, 
#if someday , it scraped all data in the net(damned it !)
#obsulutely, it's time to tie the spider on a single domain!

import re
import urllib2
from bs4 import *
from bs4 import SoupStrainer

#just our target is freebuf
#target : find all href !!! 
#only_href = SoupStrainer("a")
"""
web = urllib2.urlopen("http://www.freebuf.com/")
soup = BeautifulSoup(web.read())
for href in soup.findAll("a"):
    #print href[] #debug I/O to check if we get all tags <a>
    if "href" in href.attrs:
        #print href.attrs["href"] # debug I/O to check the forms of hrefs that you want
        #we find the target href is http://xxx.freebuf.com/
        #if you can write the regs , just do 
        #if not , learn!
"""


"""
----------------------------------------code----------------------------------------
#we just find how to deal with our href
#for better understanding, pack a function
def get_links(url):
    web = urllib2.urlopen(url)
    soup = BeautifulSoup(web.read())
    #write reg for checking the only_domain 
    return soup.findAll(href=re.compile("^(https?://[0-9a-zA-Z_]{,20}\.?freebuf.com)"))

links = get_links("http://www.freebuf.com/")
for link in links:
    if "href" in link.attrs:
        print link.attrs["href"]
----------------------------------------code----------------------------------------
#by this we can image that we can crawle the entire website
"""


"""
Obsolutely, it 's not enough to do this,
if we facing with a huge website deal with is method,
we will fail .
considering a database to store these datas is neccessary!!!
but we just use simple "set()" to store for moment

so we append something to our codes and refactor it

"""

sites = set()

def get_links(url):
    global sites
    web = urllib2.urlopen(url)
    soup = BeautifulSoup(web.read())
    #write reg for checking the only_domain 
    links = soup.findAll(href=re.compile("^(https?://[0-9a-zA-Z_]{,20}\.?freebuf.com)"))
    for link in links:
        if "href" in link.attrs:
            print link.attrs["href"]
            #deal with our data(to store it permenently or to use a database)
            sites.add(link.attrs["href"])
            
get_links("http://www.freebuf.com/")
print 
print 
print 
print 
print sites

#now the urls we got are in the only domain


