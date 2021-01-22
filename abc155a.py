# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc155_a
import sys

a,b,c = map(int,input().split()) #input:int a,b

if((a==b)and(b==c)):
	print("No")
	sys.exit()
if(a!=b)and(b!=c)and(a!=c):
	print("No")
	sys.exit()
print("Yes")
