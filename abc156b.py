# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc156_b
import sys

n,k = map(int,input().split()) #input:int a,b

tmp=n
num=0
while(tmp>0):
	num+=1
	tmp=tmp//k
print(num)
