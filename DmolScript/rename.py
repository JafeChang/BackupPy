#!/usr/bin/env python
# rename.py

import os
import os.path

names = open("names.txt","r")
for line in names:
	line.replace("\r\n","\n")
	line.replace("\r\r","\n")
	line = line[0:len(line)-1]
	l = line.split("@")
	lsrc = l[0].split("/")[1]
	fileName = lsrc[0:len(lsrc)-15]
	fileXsdSrc = l[0][0:len(l[0])-1]+"/"+fileName+".xsd"
	fileOutSrc = l[0][0:len(l[0])-1]+"/"+fileName+".outmol"
	#print os.path.exists(fileOutSrc)
	if l[2] != "":
		fileXsdDest = "dest/"+l[1]+"/"+l[2]+".xsd"
		fileOutDest = "dest/"+l[1]+"/"+l[2]+".outmol"
		if not os.path.exists("dest/"+l[1]):
			os.makedirs("dest/"+l[1])
		open( fileXsdDest , 'wb' ).write( open( fileXsdSrc , 'rb' ).read())
		open( fileOutDest , 'wb' ).write( open( fileOutSrc , 'rb' ).read())
		


