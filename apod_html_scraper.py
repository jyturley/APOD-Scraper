#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib import urlopen
import re
import os

apod_archive = BeautifulSoup(urlopen('http://apod.nasa.gov/apod/archivepix.html'))
links = apod_archive.find_all(href=re.compile('ap[0-9]*.html'))

for link in links:
	try:
		site_name = link.get('href')
		f = open('APOD/' + site_name, 'w')
		f.write(str(urlopen('http://apod.nasa.gov/apod/' + site_name).read()))
		f.close()
	except:
		print link


# from bad_apod_links import bad_links

# for link in bad_links:
# 	try:
# 		site_name = link.split('"')
# 		f = open('APOD/' + site_name[1], 'w')
# 		f.write(urlopen('http://apod.nasa.gov/apod/' + site_name[1]).read())
# 		f.close()
# 		print "SUCCESS " + link
# 	except:
# 		print "FAIL" + link