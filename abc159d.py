# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc159_d
import sys

n = int(input())
tmp = input().split()
a = list(map(lambda a: int(a), tmp))
#print(a)

numlist={}
for i in range(n):
	s= a[i]
	key_exists = s in numlist
	if(key_exists):
		numlist[s]+=1
	else:
		numlist[s]=1

total=0
for i in numlist:
	total+=numlist[i]*(numlist[i]-1)//2
for i in range(n):
	s= a[i]
	print(total-numlist[s]+1)

#print(numlist)