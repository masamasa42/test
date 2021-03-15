# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc169_d
import sys
import math

n=int(input())


if(n==1):
    print(0)
    sys.exit()

limit = math.floor(n**0.5)+1
s=[1,3,6,10,15,21,28,36,45]

total=0
for i in range(2,limit):
#    print(i)
    if(n%i==0):
#        print("------")
#        print(i)
#        print(limit)
#        print("--")
        tmp=0
        for j in range(41):
#            print(n)
            n=n//i
            tmp+=1
            if(n%i!=0):
                break
        #kari
        #total+=tmp
#        print("tmp:")
#        print(tmp)

        for k in range(len(s)):
            if(tmp<s[k]):
                total+=k
                break
#        print("total:")
#        print(total)

        if(n==1):
            break
        limit = math.floor(n**0.5)+1
    if(i>=limit-1):
        total+=1
        break
#        print(n)
#        print(tmp)


#print("----")
#print(n)
#print(limit)
print(total)