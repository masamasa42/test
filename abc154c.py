# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc154_c
import sys

n=int(input()) 
a=input().split()

a.sort()

for i in range(n-1):
    if(a[i]==a[i+1]):
            print("NO")
            sys.exit()
print("YES")