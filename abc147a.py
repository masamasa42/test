# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc147_a
import sys
#import collections

#n= int(input())
#s= input()
tmp = input().split()
a,b,c = list(map(lambda a: int(a), tmp))

if(a+b+c>21):
	print("bust")
else:
	print("win")