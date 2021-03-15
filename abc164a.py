# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc164_a
import sys

tmp = input().split()
s,w = map(lambda a: int(a), tmp)

if(s<=w):
	print("unsafe")
else:
	print("safe")