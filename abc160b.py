# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc160_b
import sys

x = int(input())

a=x//500
b=(x%500)//5
total=a*1000+b*5
print(total)
