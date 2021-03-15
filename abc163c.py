# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc163_c
import sys

n = int(input())
tmp = input().split()
a = list(map(lambda a: int(a), tmp))


num=[0]*n
for i in range(n-1):
#	print(a[i])
	num[a[i]-1]+=1

for i in range(n):
	print(num[i])