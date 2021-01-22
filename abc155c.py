# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc155c
import sys

n=int(input())

dict={}
for i in range(n):
	s=input()
	key_exists = s in dict
	if(key_exists):
		dict[s]+=1
	else:
		dict[s]=1

maxdict=0
for j in dict:
	maxdict=max(maxdict,dict[j])
ans=[]
for j in dict:
	if(maxdict==dict[j]):
		ans.append(j)
ans.sort()
for i in ans:
	print(i)
