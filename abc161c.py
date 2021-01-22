# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc161_c
import sys

tmp = input().split()
n,k = map(lambda a: int(a), tmp)

tmp=n%k
ans=min(tmp,k-tmp)
print(ans)