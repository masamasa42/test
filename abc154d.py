# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc154_d
import sys

n,k = map(int,input().split()) #input:int a,b
p = input().split()

tmp=0
for j in range(k):
    tmp+=int(p[j])
maxsum=tmp
maxindex=0

for i in range(n-k):
    tmp+=int(p[i+k])
    tmp-=int(p[i])
    if(tmp>maxsum):
        maxsum=tmp
        maxindex=i+1

total=k
for i in range(maxindex,maxindex+k):
    total+=int(p[i])
total/=2
print(total)