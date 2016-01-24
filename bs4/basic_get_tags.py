#the project is for scraping
from bs4 import SoupStrainer
from bs4 import *
import urllib2
"""

web = urllib2.urlopen("http://www.freebuf.com/")
webobj = BeautifulSoup(web.read())
namelist = webobj.findAll("a")
for name in namelist:
#    print name.get_text()   just get the textfield ,
    print name # just print all tag <a>
"""

"""
web = urllib2.urlopen("http://www.freebuf.com/")
trainer = SoupStrainer("a")  #built a parse_only object: SoupStrainer
soup = BeautifulSoup(web.read(),parse_only=trainer) #fill the parse_only field 
print  type(trainer)
namelist = soup.findAll("a")
for name in namelist:
    print name

"""

"""
but there is a more powerfull funtion to use
    just use the function: SoupStrainer
"""

