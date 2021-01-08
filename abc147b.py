# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc147_b
import sys
#import collections

#n= int(input())
s= input()
#tmp = input().split()
#a,b,c = list(map(lambda a: int(a), tmp))


total=0
for i in range(0,len(s)//2):
	if (s[i]!=s[len(s)-i-1]):
		total+=1
print(total)


