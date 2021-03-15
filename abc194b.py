# -*- coding: utf-8 -*-
#ABC194B
import sys

n=int(input())

lisa=[]
lisb=[]
minboth=200000
for i in range(n):
    a,b = map(int, input().split())
    minboth=min(minboth,a+b)
    lisa.append(a)
    lisb.append(b)

for i in range(n):
    for j in range(n):
        if(i!=j):
            minboth=min(minboth,max(lisa[i],lisb[j]))
print(minboth)
