# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc165_b
import sys

k=int(input())

total=100
ans=0
while(total<k):
	total+=total//100
	ans+=1
print(ans)
