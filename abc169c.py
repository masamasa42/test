# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc169_c
import sys
import math
from decimal import Decimal

a,b = map(Decimal, input().split())

print(math.floor(a*b))