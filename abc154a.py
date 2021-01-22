# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc154_a
import sys
import math

s,t=input().split()
a,b = map(int,input().split()) #input:int a,b
u=input()

out=""
if(s==u):
    out+=str(a-1)
    out+=" "
    out+=str(b)
if(t==u):
    out+=str(a)
    out+=" "
    out+=str(b-1)
print(out)