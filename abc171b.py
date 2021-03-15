# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc171_b
import sys

tmp = input().split()
n,k = map(lambda a: int(a), tmp)
tmp = input().split()
p = list(map(lambda a: int(a), tmp))

p.sort()

total=0
for i in range(k):
    total+=p[i]

print(total)
