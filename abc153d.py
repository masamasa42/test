# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc153_d
import sys
import math
#import collections

h = int(input())

tmp=h

cnt=0
for i in range(41):
    if(tmp//2>0):
        tmp=tmp//2
        cnt+=1
    else:
        break

print(2**(cnt+1)-1)