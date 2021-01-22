# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc155b
import sys
#import math

n=int(input())
a=list(map(int,input().split())) #input:int a,b

for i in range(n):
    if(a[i]%2==0):
        if((a[i]%3!=0)and(a[i]%5!=0)):
            print("DENIED")
            sys.exit()

print("APPROVED")


