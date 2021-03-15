# -*- coding: utf-8 -*-
import sys
import math
#ABC195b

tmp = input().split()
a,b,w = list(map(lambda a: int(a), tmp))

w*=1000
maxi=-1
mini=1000001

for i in range(1,1000001):
    if((w>=a*i)and(w<=b*i)):
        mini=min(mini,i)
        maxi=max(maxi,i)

if((mini==1001)or(maxi==-1)):
    print("UNSATISFIABLE")
    sys.exit()

print(mini,end="")
print(" ",end="")
print(maxi)



