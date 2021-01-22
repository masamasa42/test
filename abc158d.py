# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc158_d
import sys
import math

s=input()
n=int(input())

row=0 #sounyuu muki
reverse="" #sentou sounyuu you mojiretu

for i in range(n):
	tmp=input()
	if(tmp[0]=="1"):
		row+=1
		row%=2
	else:
		a,b,c=tmp.split()
		f=(int(b)+row)%2
		if(f==0):
			s=s+c
		else:
			reverse=reverse+c

#querry wo subete syori siowatte kara sentou ni sounyuu
tmp=""
for i in range(len(reverse)):
	tmp+=(reverse[len(reverse)-i-1])
s=tmp+s

#syuturyoku
if(row==0):
	print(s)
else:
	tmp=""
	for i in range(len(s)):
		tmp+=(s[len(s)-i-1])
	print(tmp)



