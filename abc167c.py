# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc167_c
import sys

n,m,x = map(int, input().split())

c = [0]*n
a = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
	s = list(map(int, input().split()))
	c[i]=s[0]
	for j in range(m):
		a[i][j]=s[j+1]
#	print(s)

#print(c)
#print(a)

ans=-1
for i in range(2**n): #ビット全探索
	totalcost=0
	totala=[0]*m
#	print("---")
#	print(i)
	for j in range(n):
		if ((i>>j) & 1):
#			print(1)
			totalcost+=c[j]
			for k in range(m):
				totala[k]+=a[j][k]
#		else:
#			print(0)
#	print(totala)
#	print(totalcost)
	for j in range(m):
		if(totala[j]<x):
			break
		if(j==m-1):
#			print("hoge")
			if(ans==-1):
				ans=totalcost
			else:
				ans=min(ans,totalcost)
print(ans)
