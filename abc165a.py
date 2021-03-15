# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc165_a
import sys

k=int(input())
a,b = map(int, input().split())

if(a%k==0):
	print("OK")
	sys.exit()
if(b%k==0):
	print("OK")
	sys.exit()

if(b//k-a//k>0):
	print("OK")
else:
	print("NG")
