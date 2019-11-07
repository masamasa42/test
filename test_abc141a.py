# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc141_a
import sys
#import collections

#n= int(input())
s= input()
#tmp = input().split()
#a = list(map(lambda a: int(a), tmp))

for i in range(len(s)):
	if(i%2==0):
		if(s[i]=="L"):
			print("No")
			sys.exit()
	else:
		if(s[i]=="R"):
			print("No")
			sys.exit()
		
print("Yes")

#test adding line
