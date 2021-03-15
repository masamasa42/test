# -*- coding: utf-8 -*-
#ABC195c
import sys
import math

n = input()
tmp=len(n)
n = int(n)

#print(n-int(10**(tmp-1)))

ans=0
ans+=((tmp-1)//3)*(n-int(10**(tmp-1))+1)

#print(ans)
if(tmp>=4):
    ans+=0
if(tmp>=5):
    ans+=9000*1
if(tmp>=6):
    ans+=90000*1
if(tmp>=7):
    ans+=900000*1
if(tmp>=8):
    ans+=9000000*2
if(tmp>=9):
    ans+=90000000*2
if(tmp>=10):
    ans+=900000000*2
if(tmp>=11):
    ans+=9000000000*3
if(tmp>=12):
    ans+=90000000000*3
if(tmp>=13):
    ans+=900000000000*3
if(tmp>=14):
    ans+=9000000000000*4
if(tmp>=15):
    ans+=90000000000000*4
if(tmp>=16):
    ans+=900000000000000*4


print(ans)
#print(tmp)
#print(n)

