#!/usr/bin/env python
# maxSublist.py

#-------------------------------------
#list N = {A1,A2,A3,...,AN}
#to get the max of function f(i,j)
#f(i,j)=max{0,sum(Ak,k=i:j)}
#-------------------------------------

import math
import random
import time

def current_milli_time() : 
	return int(round(time.time() * 1000))

def getListInt(n,start = -99, end = 100):
	l=[]
	for i in range(0,n):
		l.append(random.randint(start,end))
	return l

def getList100():
	l = [-66, 13, 98, -68, -39, -48, -45, -56, 33, 41, -72, -41, -63, 55, -44, -95, 3, -25, -78, -81, -71, 40, -8, 51, 16, 73, 48, 11, 87, 6, -46, -53, -42, -81, 57, 83, 100, -74, 88, -66, 91, 37, 74, 95, -58, -32, -80, -92, 47, -57, 98, 86, 82, 84, -77, -46, -11, -79, 51, -34, 86, 92, 21, -54, 82, -86, 20, 47, -29, -32, -50, -13, 8, -18, -58, 98, -57, -3, -73, 29, -61, 78, -25, -83, -41, 43, 94, -13, 76, 57, -34, 73, 42, -31, 15, 20, 2, -11, -94, 68]
	return l

def getSum(l):
	sum = 0
	for i in l:
		sum += i
	return sum

def getMaxSublist1(l):
	max = 0
	maxSL = []
	for i in range(0,len(l)):
		for j in range(i,len(l)):
			max = getSum(l[i:j+1])
			if max > 0:
				maxSL.append(max)
			else:
				maxSL.append(0)
	if len(l) > 0:
		max = l[0]
	else:
		return 0
	for i in maxSL:
		if max < i:
			max = i
	return max

def getMaxSublist2(l):
	max = 0
	for i in range(0,len(l)):
		sum = 0
		for j in range(i,len(l)):
			sum += l[j]
			if max < sum:
				max = sum
	return max

def getMaxSublist3(l):
	n = len(l)
	if n > 1:
		h = n/2
		maxL = getMaxSublist3(l[0:h])
		maxR = getMaxSublist3(l[h:n])
		maxLR = 0
		maxLR1 = 0
		maxLR2 = 0
		sumL = 0
		sumR = 0
		for i in range(h-1,-1,-1):
			sumL += l[i]
			if maxLR1 < sumL:
				maxLR1 = sumL
		for j in range(h,n):
			sumR += l[j]
			if maxLR2 < sumR:
				maxLR2 = sumR
		maxLR = maxLR1 + maxLR2
		return max([maxL,maxR,maxLR])
	else:
		#print 
		return max(0,l[0])

def getMaxSublist4(l):
	negCnt = 0
	for i in l:
		if i<0:
			negCnt += 0
	if negCnt == len(l):
		return
	max = 0
	sum = 0
	for j in range(0,len(l)):
		sum += l[j]
		if max < sum:
			max = sum
		elif sum < 0:
			sum = 0
	return max




l = getListInt(1000000)
#l = [4,-3,5,-2,-1,2,6,-2]
#l = [-2, 11,-4, 13, -5, -2]
t0 = current_milli_time()
#a1 = getMaxSublist1(l)
t1 = current_milli_time()
#a2 = getMaxSublist2(l)
t2 = current_milli_time()
a3 = getMaxSublist3(l)
t3 = current_milli_time()
a4 = getMaxSublist4(l)
t4 = current_milli_time()
#print a1,"[1:",t1-t0,"milliseconds]"
#print a2,"[2:",t2-t1,"milliseconds]"
print a3,"[3:",t3-t2,"milliseconds]"
print a4,"[4:",t4-t3,"milliseconds]"
#print 
#print range(3,-1,-1)