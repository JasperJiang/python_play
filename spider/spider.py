# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup

url_or = 'http://www.zmz2017.com'
req = urllib2.Request('http://www.zmz2017.com')


resp = urllib2.urlopen(req)
soup = BeautifulSoup(resp.read(), 'lxml')

top24_soup = soup.select('.top24 ul li a')

top24 = []

for x in range(len(top24_soup)):
    top24.append({'name':top24_soup[x].get_text()})

for x in range(len(top24_soup)):
    top24[x]['href'] = url_or+top24_soup[x]['href']

print top24