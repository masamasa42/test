# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc151_b
import sys
import math
#import collections

#n= int(input())
#s= input()
tmp = input().split()
n,k,m = list(map(lambda a: int(a), tmp))

tmp = input().split()
a = list(map(lambda a: int(a), tmp))

total=0
for i in range(0,n-1):
    total+=a[i]
ans=n*m-total

if(ans<0):
    print(0)
elif(ans>k):
    print(-1)
else:
    print(ans)