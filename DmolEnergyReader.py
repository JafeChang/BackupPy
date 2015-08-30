#!/usr/bin/env python
# DmolEnergyReader.py

import os
import os.path

fileroot=os.listdir(".")
for filesize in fileroot:
	if os.path.isdir(filesize):
		#print filesize
		filenos=os.listdir(filesize)
		for fileno in filenos:
			if os.path.isdir(filesize+"/"+fileno):
				#print "|\t"+fileno
				fileouts = os.listdir(filesize+"/"+fileno)
				for outmol in fileouts:
					if outmol.endswith(".outmol"):
						#print "|\t"+"|\t"+outmol
						file_obj=open(filesize+"/"+fileno+"/"+outmol)
						linenumber = 0
						totalenergy = 0
						zeroenergy = 0
						hasEnergyAtThisLine = 0
						isMS61 = 0
						isSuccessful = "false"
						for line in file_obj:
							linenumber += 1
							if linenumber == 3 and line.find("Materials Studio DMol^3 version 6.1") != -1:
								isMS61 = 1
							if line.find("Message: DMol3 job finished successfully"):
								isSuccessful = "true"
							if line.startswith("       Cycle    Total Energy   Energy ") and hasEnergyAtThisLine == 0:
								hasEnergyAtThisLine = 1
							if line.startswith("opt==") and hasEnergyAtThisLine == 1:
								line = line[0:len(line)-1]
								energies = line.split(" ")
								for i in range(len(line)):
									if energies.count("")>0:
										energies.remove("")
									if energies.count("opt==")>0:
										energies.remove("opt==")
									totalenergy = energies[1]
								hasEnergyAtThisLine = 0
							if line.startswith("   Zero point vibrational energy: "):
								line = line[33:len(line)-1]
								zenergys = line.split(" ")
								for i in range(len(zenergys)):
									if zenergys.count("")>0:
										zenergys.remove("")
								zenergys.remove("kcal/mol")
								zeroenergy = zenergys[0]

						print fileno+"\t"+outmol[0:-7],"\t",totalenergy,"\t",zeroenergy,"\t",isSuccessful

os.system("PAUSE")