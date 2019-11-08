# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc129/tasks/abc129_b
import sys

n= int(input())
#s= input()
tmp = input().split()
w = list(map(lambda a: int(a), tmp))

sum=0
for i in range(n):
	sum+=w[i]
#w.sort()
ave=sum//2

#print(w)

sum2=0
for i in range(n):
	sum2+=w[i]
	if(sum2>ave):
		if((2*sum2-sum)>(sum-2*sum2+2*w[i])):
			print(sum-2*sum2+2*w[i])
			sys.exit()
		else:
			print(2*sum2-sum)
			sys.exit()
