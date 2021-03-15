# -*- coding: utf-8 -*-
#ABC194D
import sys


n= int(input())

ans=0
for i in range(1,n):
    ans+=n/(n-i)
print(ans)


