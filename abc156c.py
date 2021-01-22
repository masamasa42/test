# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc156_c
import sys

n = int(input())
x = list(map(int,input().split())) #input:int a,b

#print(n)
#print(x)

mintotal=0
for i in range(1,101):
	total=0
	for j in range(n):
		total+=(i-x[j])**2
	if i ==1:
		mintotal=total
	mintotal = min (mintotal,total)
print(mintotal)


