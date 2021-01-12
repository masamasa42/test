# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc149_c
import sys

n= int(input())
if(n==2):
    print(2)
    exit()

for i in range (0,100000):
    tmp=n+i
    for p in range(2,tmp):
        if tmp % p == 0:
            break
        if(p==tmp-1):
            print(tmp)
            exit()
