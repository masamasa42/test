# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc160_c
import sys

tmp = input().split()
k,n = map(lambda a: int(a), tmp)
tmp = input().split()
a = list(map(lambda a: int(a), tmp))

maxd=k-a[n-1]+a[0]
for i in range(1,n):
	maxd=max(maxd, a[i]-a[i-1])

print(k-maxd)
