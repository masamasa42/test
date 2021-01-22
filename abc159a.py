# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc159_a
import sys

n,m = map(int, input().split())

total=n*(n-1)//2+m*(m-1)//2
print(total)