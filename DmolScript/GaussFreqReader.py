#!/usr/bin/env python
# GaussFreqReader.py

import os
import os.path

class Mode(object):
	pass

fileroot=os.listdir(".")
output = open("out.txt","w")
for dirname in fileroot:
	if os.path.isdir(dirname):
		files=os.listdir(dirname)
		for logfile in files:
			if logfile.endswith(".log"):
				output.writelines("Isomer "+dirname+"-"+logfile[0:len(logfile)-4]+"\n")
				file_obj=open(dirname+"/"+logfile)
				linenumber = 0
				ANClineNo = 0
				modeNo = 0
				headFreq = 0 #havn't come across
				modeList=[]
				for line in file_obj:
					linenumber += 1 
					if line.startswith(" and normal coordinates:") and headFreq == 0:
						headFreq = 1 # just come across
						ANClineNo = linenumber
					if line.startswith(" - Thermochemistry -") and headFreq == 1:
						headFreq = -1 # say goodbye to freq.
					if line.startswith(" Frequencies --") and headFreq == 1:
						line = line[0:len(line)-1]
						fres = line.split(" ")
						for i in range(len(fres)):
							if fres.count("")>0:
								fres.remove("")
							if fres.count("Frequencies")>0:
								fres.remove("Frequencies")
							if fres.count("--")>0:
								fres.remove("--")
						for fre in fres:
							modeNo += 1
							mode = Mode()
							mode.fre=round(float(fre),1)
							mode.no = modeNo
							modeList.append(mode)
					if line.startswith(" IR Inten    --") and headFreq == 1:
						line = line[0:len(line)-1]
						irs = line.split(" ")
						for i in range(len(irs)):
							if irs.count("")>0:
								irs.remove("")
							if irs.count("IR")>0:
								irs.remove("IR")
							if irs.count("Inten")>0:
								irs.remove("Inten")
							if irs.count("--")>0:
								irs.remove("--")
						if modeNo%3 == 0:
							modeNoIr = modeNo - 3
						else:
							modeNoIr = 3*(modeNo/3)
						for ir in irs:
							modeNoIr += 1
							#modeList[modeNoIr-1].ir=round(float(ir),2)
							modeList[modeNoIr-1].ir = "%.2f"%float(ir)
				output.writelines("mode             cm-1        km/mol\n")
				for mode in modeList:
					noGap = 4
					freGap = 12
					irGap = 8
					if mode.no >= 10:
						noGap = 3
					if mode.fre >=100.0 or mode.fre < -10.0:
						freGap = 11
					if float(mode.ir) >= 100.0:
						irGap = 6
					elif float(mode.ir) >= 10.0:
						irGap = 7
					output.writelines(" "*noGap+str(mode.no)+" "*freGap+str(mode.fre)+" "*irGap+str(mode.ir)+"\n")
				output.writelines("\n")
output.close()
os.system("PAUSE")