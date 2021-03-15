# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc164_c
import sys

n=int(input())
dictio={}
for i in range(n):
	tmp=input()
#	print(tmp)
	if(tmp in dictio):
		dictio[tmp]+=1
#		print(dictio[tmp])
	else:
		dictio[tmp]=1
#		print(dictio[tmp])
print(len(dictio))