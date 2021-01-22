# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc156_d
import sys
from operator import mul
from functools import reduce
mod =1000000007

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    over%=mod
    return (over // under)%mod

#n = int(input())
n,a,b = list(map(int,input().split())) #input:int a,b

if(n==2):
	print(0)
	sys.exit()

total=1
for i in range(n):
	total*=2
	if(total>mod):
		total%=mod
total-=1

#print(total)

total -= cmb(n, a)
total -= cmb(n, b)

print(total)
#print(n)
#print(x)

