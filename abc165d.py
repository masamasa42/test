# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc165_ｄ
import sys
import math

a,b,n = map(int, input().split())

if(b>n):
	print(math.ceil(a*n//b))
elif(b==1):
	print(0)
else:
	print(math.ceil(a*(b-1)//b))




