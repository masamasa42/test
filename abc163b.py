# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc163_b
import sys

tmp = input().split()
n,m = map(lambda a: int(a), tmp)
tmp = input().split()
a = list(map(lambda a: int(a), tmp))

total=0
for i in range(m):
	total+=a[i]

total=n-total
if(total<0):
	print(-1)
else:
	print(total)