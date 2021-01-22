# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc153_b
import sys
import math
#import collections

tmp = input().split()
h,n = list(map(lambda a: int(a), tmp))
tmp = input().split()
a = list(map(lambda a: int(a), tmp))

total=0
for i in range(0,n):
    total+=a[i]

if(total>=h):
    print("Yes")
else:
    print("No")