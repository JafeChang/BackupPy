#!/usr/bin/python
#coding: UTF-8

import os
import os.path
import time

class Filetype(object):
	#typename = ""
	#extension = []
	#lineCnt = 0
	pass

global dirList
global banList
global filetypeList

def hasType(tp):
	global filetypeList
	for ext in filetypeList:
		if ext.typename == tp:
			return 1
	return 0

def getType(tp):
	global filetypeList
	for ext in filetypeList:
		if ext.typename == tp:
			return ext
	return 

def readConfig():
	configure = open("configure.txt","r")
	dirOrExt = 0  # 0-none ;1-dir; 2-ext;
	global dirList
	global banList
	global filetypeList
	dirList = []
	banList = []
	filetypeList = []
	for line in configure:
		line.replace("\r\n","\n")
		line.replace("\n\r","\n")
		line = line[0:len(line)-1]
		if line == "#directories list":
			dirOrExt = 1
		if dirOrExt == 1 and (not line.startswith("#")):
			if line != "" and not line.startswith("!"):
				dirList.append(line)
			if line != "" and line.startswith("!"):
				banList.append(line[1:len(line)])
		if line == "#extensions list":
			dirOrExt = 2	
		if dirOrExt == 2 and (not line.startswith("#")):
			if line != "" :
				exts = line.split("@")
				
				if hasType(exts[1]) == 0:
					filetype = Filetype()
					filetype.typename = exts[1]
					filetype.extensions = [exts[0].lower()]
					filetype.count = 0
					filetypeList.append(filetype)
				else:
					filetype = getType(exts[1])
					if filetype.extensions.count(exts[0].lower())==0:
						filetype.extensions.append(exts[0].lower())
	configure.close()

def getDir(directory):
	if banList.count(directory)!=0:
		return
	if os.path.isdir(directory):
		for lowDir in os.listdir(directory):
			getDir(directory+"/"+lowDir)
	else:
		readFile(directory)

def readFile(file):
	filenames = file.split(".")
	extname = "."+filenames[-1]
	hasThisExt = 0
	theVeryType = Filetype()
	for filetype in filetypeList:
		for ext in filetype.extensions:
			if ext == extname:
				hasThisExt = 1
				theVeryType = filetype
	if hasThisExt == 0:
		return
	else:
		cnt = 0
		codeFile = open(file,"r")
		for line in codeFile:
			line.replace("\r\n","\n")
			line.replace("\n\r","\n")
			if line != "\n":
				cnt += 1
		theVeryType.count += cnt
		codeFile.close()
		
readConfig()
for directory in dirList:
	getDir(directory)
logfile = open("How Many Codes.log","a")
logfile.writelines(time.strftime("%Y-%m-%d %X")+"\n")
for filetype in filetypeList:
	logfile.writelines(filetype.typename+"\t"+str(filetype.count)+"\n")
logfile.writelines("-------------------------------------\n\n")
logfile.close()


