# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc169_b
import sys

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
	if(a[i]==0):
		print(0)
		sys.exit()

ans=1
for i in range(n):
	ans*=a[i]
	if(ans>1000000000000000000):
		print(-1)
		sys.exit()
print(ans)