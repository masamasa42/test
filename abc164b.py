# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc164_b
import sys

tmp = input().split()
a,b,c,d = map(lambda a: int(a), tmp)

while(1):
	c=c-b
	if(c<=0):
		print("Yes")
		sys.exit()
	a=a-d
	if(a<=0):
		print("No")
		sys.exit()

