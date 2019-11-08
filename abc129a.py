# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc129/tasks/abc129_a
import sys

#n= int(input())
#s= input()
tmp = input().split()
p,q,r = list(map(lambda a: int(a), tmp))

sum = p+q+r-max(p,max(q,r))
print(sum)