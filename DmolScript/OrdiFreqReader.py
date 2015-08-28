#!/usr/bin/env python
# OrdiFreqReader.py

import os
import os.path

clusfile = open("clusfile.txt","w")
freqfile = open("freqfile.txt","w")
for sizefile in os.listdir("dest"):
	if os.path.isdir(sizefile):
		for outfile in os.listdir("dest/"+sizefile):
			if outfile.endswith(".outmol"):
				f = open("dest/"+sizefile+"/"+outfile,"r")
				#print "dest/"+sizefile+"/"+outfile
				pos = 0 # 1 - coordinates ; 3 - frequencies
				pin = 0
				linecnt = 0
				cluster = []
				freq = []
				for line in f:
					line=line[0:len(line)-1]
					linecnt += 1

					if line.endswith("Final Coordinates (Angstroms)") and pos!=1:
						#print outfile,linecnt
						pos = 1
						pin = linecnt
					if pos == 1 and not line.endswith("-"*70) and pin<linecnt-2 :
						atom = line.split(" ")
						while atom.count("") > 0 :
							atom.remove("")
						#['1', 'Al', '1.398684', '-0.331397', '1.472207']
						#print atom
						cluster.append(atom)
					if pos == 1 and line.endswith("-"*70) and pin<linecnt-2:
						pos = 2
					if line.endswith("vibrational frequencies, intensities") and pos!=3:
						pos =3
						pin = linecnt
					if pos == 3 and line!="" and pin<linecnt-1:
						mode = line.split(" ")
						while mode.count("") > 0:
							mode.remove("")
						freq.append(mode)
					if pos == 3 and line=="" and pin<linecnt-1:
						pos = 4
				f.close()
				clusfile.writelines("Isomer "+outfile[0:-7]+"\n")
				freqfile.writelines("Isomer "+outfile[0:-7]+"\n")
				for atom in cluster:
					if(float(atom[0])>9):
						a=7
					else:
						a=8
					b=[8,8,8]
					for i in range(0,3):
						if float(atom[i+2])>=10.0 or (float(atom[i+2])<0.0 and float(atom[i+2])>-10.0):
							b[i] = 7
						elif float(atom[i+2]) <=-10:
							b[i] = 6
					clusfile.writelines(atom[0]+" "*a+atom[1]+" "*b[0]+atom[2]+" "*b[1]+atom[3]+" "*b[2]+atom[4]+"\n")
				clusfile.writelines("\n")
				for mode in freq:
					if int(mode[0])>9:
						c = 7
					else:
						c = 8
					if float(mode[2])>=100.0:
						d = 8
					else:
						d = 9
					if float(mode[3])>=10.0:
						e = 7
					else:
						e = 8 
					freqfile.writelines(mode[0]+" "*c+mode[1]+" "*d+mode[2]+" "*e+mode[3]+"\n")
				freqfile.writelines("\n")
clusfile.close()
freqfile.close()

						
