# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc150_b
import sys

n= int(input())
s= input()

total=0
for i in range(0,n-2):
    if((s[i]=="A")and(s[i+1]=="B")and(s[i+2]=="C")):
        total+=1
print(total)
