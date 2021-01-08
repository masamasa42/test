# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc147/tasks/abc147_d
import sys
#import collections

n= int(input())

tmp = input().split()
s = list(map(lambda a: int(a), tmp))

total=0
a=[]
for i in range(0,60):
	a.append(0)

for i in range(0,n):
	tmp = s[i]
	for j in range(0,60):
		if(tmp==0):
			break
		if(tmp%2==1):
			a[j]+=1
		tmp=tmp//2

total=0
for j in range(60,0,-1):
	total*=2
	if(a[j-1]>0):
		total=total+(a[j-1])*(n-a[j-1])
	if(total>1000000007):
		total=total%1000000007
total=total%1000000007

print(total)



