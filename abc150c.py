# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc150_c
import sys
import math
#import collections

n= int(input())
#s= input()
tmp = input().split()
#for i in range(n):
a = list(map(lambda a: int(a), tmp))

hoge1=[]
total1=0
for i in range(n):
    hoge1.append(1)
for i in range(n):
    hoge1[a[i]-1]=0
    count=0
    for j in range(a[i]):
        if(hoge1[j]==1):
            count+=1
#    print(count)
#    print(n-i)
#    print(math.factorial(n-i-1))
#    print(count*math.factorial(n-i-1))
#    print("---")
    total1+=count*math.factorial(n-i-1)
#print(total1)

tmp = input().split()
a = list(map(lambda a: int(a), tmp))
hoge2=[]
total2=0
for i in range(n):
    hoge2.append(1)
for i in range(n):
    hoge2[a[i]-1]=0
    count=0
    for j in range(a[i]):
        if(hoge2[j]==1):
            count+=1
    total2+=count*math.factorial(n-i-1)
#print(total2)

print(abs(total1-total2))

