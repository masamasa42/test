# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc151_c
import sys
import math
#import collections

#n= int(input())
#s= input()
tmp = input().split()
n,m = list(map(lambda a: int(a), tmp))

ans=[]
anstry=[]

for i in range(n):
    ans.append(0)
    anstry.append(0)
for i in range(m):
    tmp = input().split()
    index=int(tmp[0])
    if (tmp[1]=="WA"):
        if(ans[index-1]==0):
            anstry[index-1]+=1
    else:
        ans[index-1]=1

num_ans=0
num_try=0
for i in range(n):
    num_ans+=ans[i]
    if(ans[i]==1):
        num_try+=anstry[i]
out=str(num_ans)+" "+str(num_try)
print(out)

