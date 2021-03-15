# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc167_d
import sys

n,k = map(int, input().split())
a = list(map(int, input().split()))

b= [0]*(n+1)
seen= [0]*(n+1)


#print(a)
#print(b)
#print(k)
#print(seen)
#print("---")

now=1
seen[1]=1

loopcnt=0
while(k>0):
	new=a[now-1]
	loopcnt+=1

	#print(seen[now])
	#print(seen[new])
	if((seen[now]==1) and (seen[new]==1)):
		loopcnt=0
	if((seen[now]==2) and (seen[new]==2)):
		#print("---")
		#print(loopcnt)
		#print("---")
		k=((k-1)%loopcnt)+1

	now=new
	seen[now]+=1

	k-=1
#print(seen)
print(now)
