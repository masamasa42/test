# -*- coding: utf-8 -*-
#ABC194C
import sys
 
n=int(input())
tmp = input().split()
a = list(map(lambda a: int(a), tmp))
 
lis = [0 for i in range(401)]
ans=0
for i in range(n):
    lis[a[i]+200]+=1
#    print(a[i])

for i in range(400):
    for j in range(i+1,401):
        if(lis[i]>0):
            if(lis[j]>0):
                ans+=lis[i]*lis[j]*((j-i)**2)
#                print(lis[i])
#                print(lis[j])
#                print((j-i)**2)
#                print("---")

#for i in range(n-1):
#    for j in range(i,n):
#        ans+=(a[j]-a[i])**2

#print(lis)
print(ans)