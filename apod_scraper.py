#!/usr/bin/env python

from urllib import urlopen
from urllib import urlretrieve
import urlparse
import os
import glob

CURRENTPATH = '/Users/fatttmonkey/Documents/Hack/'
OUTFOLDER = '/Users/fatttmonkey/Documents/Hack/APOD/image/'

htmls = glob.glob("APOD/ap*.html")
total_len = len(htmls)
current = 1

def find_src(row):
	src = ""
	for item in row.split('"'):
		if item.lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".tiff", ".ico")):
			src = item
	return src

for html in htmls:
	try:
		f = open(html, "r")
		parsed = list(urlparse.urlparse('http://apod.nasa.gov/apod/' + html))
		for row in f:
			if "=\"image" in row:
				src = find_src(row)
				if os.path.exists(CURRENTPATH + 'APOD/' + src):
					continue
				split = src.split("/")
				filename = split[-1]
				tree_size = len(split)
				if (tree_size == 1):
					print "THIS SHOULD NEVER HAPPEN"
					print split
				if (tree_size == 2):
					directory = OUTFOLDER
				if (tree_size > 2):
					sofar = 1
					folder = OUTFOLDER
					while (sofar < tree_size-1):
						folder += split[sofar] + "/"
						sofar = sofar + 1
						if not os.path.exists(folder):
							os.makedirs(folder)
					directory = folder
				parsed[2] = src
				outpath = os.path.join(directory, filename)
				urlretrieve(urlparse.urlunparse(parsed), outpath)
		f.close()
		print str(current) + "/" + str(total_len)
		current += 1
	except:
		print "FAIL: " + html
