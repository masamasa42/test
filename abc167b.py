# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc167_b
import sys

a,b,c,k = map(int, input().split())

if(k<=a):
	print(k)
elif(k<=a+b):
	print(a)
else:
	print(a-(k-a-b))
