 # -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc164_d
import sys

s=input()
#print(s)

n=len(s)
keta=1
tmp=0
ans=[0]*(n+1)
for i in range(n):
	#print(s[n-i-1])
	tmp+=int(s[n-i-1])*keta

	#print(tmp)
	ans[n-i-1]=tmp%2019
	keta*=10
	keta%=2019
#print(ans)

total=0
modlist=[0]*(2019)
for i in range(n+1):
	modlist[ans[i]]+=1
for i in range(2019):
	tmp=modlist[i]
	if(tmp>=2):
		total+=tmp*(tmp-1)//2

#for i in range(n):
#	for j in range(i+1,n+1):
#		if(ans[i]==ans[j]):
#			total+=1

print(total)