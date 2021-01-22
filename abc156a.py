# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc156_a
import sys

n,r = map(int,input().split()) #input:int a,b

if(n>=10):
	print(r)
else:
	print(r+1000-100*n)