# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc150_a
import sys

tmp = input().split()
a,b = list(map(lambda a: int(a), tmp))

if(a*500>=b):
    print("Yes")
else:
    print("No")
