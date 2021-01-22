# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc159_b
import sys

s=input()
n=len(s)


for i in range(n//2):
	if(s[i]!=s[n-i-1]):
		print("No")
		sys.exit()
for i in range((n-1)//2):
	if(s[i]!=s[(n-1)//2-i-1]):
		print("No")
		sys.exit()
for i in range((n+3)//2,n):
	if(s[i]!=s[n-i-1]):
		print("No")
		sys.exit()
print("Yes")