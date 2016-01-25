#the problem is that we find all urls,
#i want distinguish the imsite(local server) urls and exsite urls
#what should we do?
import re
import urllib2
from bs4 import *


def get_local_links(url):
    sites = set()
    web = urllib2.urlopen(url)
    soup = BeautifulSoup(web.read())
    #write reg for checking the only_domain 
    links = soup.findAll(href=re.compile("^(https?://)"))
    for link in links:
        if "href" in link.attrs:
            if "freebuf.com" in link.attrs["href"].replace("//","").split("/")[0]:
                print link.attrs["href"]
                #deal with our data(to store it permenently or to use a database)
                sites.add(link.attrs["href"])
    return sites

def get_remote_links(url):
    sites = set()
    web = urllib2.urlopen(url)
    soup = BeautifulSoup(web.read())
    #write reg for checking the only_domain 
    links = soup.findAll(href=re.compile("^(https?://)"))
    for link in links:
        if "href" in link.attrs:
            if "freebuf.com" not in link.attrs["href"].replace("//","").split("/")[0]:
                print link.attrs["href"]
                #deal with our data(to store it permenently or to use a database)
                sites.add(link.attrs["href"])
    return sites    

get_remote_links("http://www.freebuf.com/")