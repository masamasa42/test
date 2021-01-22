# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc153_c
import sys
import math
#import collections

tmp = input().split()
n,k = list(map(lambda a: int(a), tmp))
tmp = input().split()
a = list(map(lambda a: int(a), tmp))

a.sort()
total=0
for i in range(n-k):
    total+=a[i]

print(total)