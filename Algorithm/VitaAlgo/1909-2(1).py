# 애틋한 친구 (Level 1)

import sys

def friends():
	global xlist, ylist
	distance = 0
	f1, f2 = 0, 0
	for i in range(len(xlist)):
		for j in range(i+1, len(ylist)):
			if distance < ((xlist[i]-xlist[j])**2 + (ylist[i]-ylist[j])**2):
				distance = (xlist[i]-xlist[j])**2 + (ylist[i]-ylist[j])**2
				f1, f2 = i, j
			elif distance == ((xlist[i]-xlist[j])**2 + (ylist[i]-ylist[j])**2):
				if xlist[f1] > xlist[i]:
					f1, f2 = i, j
				elif xlist[f1] == xlist[i] and ylist[f2] > ylist[j]:
					f1, f2 = i, j
	return "%d %d" %(f1+1, f2+1)

num = int(input())
xlist = [0]*num
ylist = [0]*num
for i in range(num):
	x,y = map(int, input().split())
	xlist[i] = x
	ylist[i] = y

print(friends())
