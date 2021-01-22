# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc158_c
import sys
import math

a,b = map(int, input().split())

ac=math.ceil(a*12.5)

for i in range(12):
	if(((ac+i)*0.1-b<1)and((ac+i)*0.1>=b)):
		print(ac+i)
		sys.exit()
print(-1)