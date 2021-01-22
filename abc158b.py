# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc158_b
import sys

n,a,b = map(int, input().split())

set=n//(a+b)

if(n%(a+b)>=a):
	total=(set+1)*(a)
else:
	total=set*(a)+n%(a+b)
print(total)

