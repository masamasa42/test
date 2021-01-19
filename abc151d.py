# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc141/tasks/abc151_d
import sys
import math
#import collections
from collections import deque

H,W = map(int,input().split()) #input:int a,b
maze = [input() for _ in range(H)]#input 12345 wo H gyou

distance = [[0 for i in range(W)] for j in range(H)]

ans=0
for i in range(H):
    for j in range(W):
        if maze[i][j]=="#":
            continue
        distance = [[-1 for i in range(W)] for j in range(H)]

        stack = deque([[i,j]])
        distance[i][j] = 0

        while stack:
            h,w = stack.popleft()
            for tmpx,tmpy in [[0,1],[0,-1],[1,0],[-1,0]]:
                new_h, new_w = h+tmpy, w+tmpx
                if new_h < 0 or new_w < 0 or new_h >= H or new_w >= W:
                    continue
                elif maze[new_h][new_w] != "#" and distance[new_h][new_w] == -1:
                    distance[new_h][new_w] = distance[h][w]+1
                    stack.append([new_h, new_w])
        for k in range(H):
            for l in range(W):
                ans = max(ans, distance[k][l])

print(ans)

#for i in range(H):
#    print(maze[i])
#for i in range(H):
#    print(distance[i])


#n= int(input())
#s= input()
#tmp = input().split()
#n,m = list(map(lambda a: int(a), tmp))

#ans=[]
#anstry=[]

#for i in range(n):
#    ans.append(0)
#    anstry.append(0)
#for i in range(m):
#    tmp = input().split()
#    index=int(tmp[0])
#    if (tmp[1]=="WA"):
#        if(ans[index-1]==0):
#            anstry[index-1]+=1
#    else:
#        ans[index-1]=1

#num_ans=0
#num_try=0
#for i in range(n):
#    num_ans+=ans[i]
#    if(ans[i]==1):
#        num_try+=anstry[i]
#out=str(num_ans)+" "+str(num_try)
#print(out)

