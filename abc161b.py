# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc161_b
import sys

tmp = input().split()
n,m = map(lambda a: int(a), tmp)
tmp = input().split()
a = list(map(lambda a: int(a), tmp))

total=0
for i in range(n):
	total+=a[i]
ave=total/4/m
count=0
for i in range(n):
	if(a[i]>=ave):
		count+=1

if(count>=m):
	print("Yes")
else:
	print("No")
