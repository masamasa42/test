# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc149_b
import sys
tmp = input().split()
a,b,c = list(map(lambda a: int(a), tmp))

if(a>c):
    print(a-c,b)
elif(a+b>c):
    print(0,a+b-c)
else:
    print(0,0)
