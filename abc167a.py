# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc167_a
import sys

s=input()
t=input()

ans=1
for i in range(len(s)):
	if(s[i]!=t[i]):
		ans=0
if (ans == 1):
	print("Yes")
else:
	print("No")