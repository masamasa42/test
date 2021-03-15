 # -*- coding: utf-8 -*-
#ABC195A
import sys
import math

tmp = input().split()
m,h = list(map(lambda a: int(a), tmp))

if(h%m==0):
    print("Yes")
else:
    print("No")


