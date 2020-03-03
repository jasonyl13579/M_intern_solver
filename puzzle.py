# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:15:13 2020

@author: Corn
"""

A1 = [['.']*3 for i in range(3)] 
A2 = [['*']*3 for i in range(3)] 

for i in range(3):
    for j, n in enumerate(input()):
        A1[i][j] = n
input()
for i in range(3):
    for j, n in enumerate(input()):
        A2[i][j] = n

def toMask(A):
    mask = 0
    count = 0 
    for i, col in enumerate(A):
        for j, n in enumerate(col):
            if n == '*':
                count += 1
                mask |= 1 << (3*i+j) 
    return mask, count
'''
A1[0][1] = A1[0][2] = A1[1][1] = '*'
A2[1][0] = A2[2][0] = A2[2][1] = '.'
for i in A1: print(i)
for i in A2: print(i)
rotated = zip(*A1[::-1])
for i in rotated: print(i)
'''
p1, c1 = toMask(A1) 
p2, c2 = toMask(A2)
ans = 0
if c1 + c2 != 9: 
    pass
elif c1 <= 2 or c2 <= 2:
    ans = 1
else:
    if c1 > c2:
        c1, c2 = c2, c1
        p1, p2 = p2, p1
        A1, A2 = A2, A1
    p2 = ((1 << 9) - 1 - p2)
    while p2 & 1 == 0:
        if p2 & (1 << 3 | 1 << 6):
            if p2 & (1 << 1 | 1 << 2):
                break
            else:
                p2 = p2 >> 3
        else:
            p2 = p2 >> 1
    #print (bin(p2))
    for d in range(4):
        A1 = list(zip(*A1[::-1]))
        p1, c1 = toMask(A1)
        while p1 & 1 == 0:
            if p1 & (1 << 3 | 1 << 6):
                if p1 & (1 << 1 | 1 << 2):
                    break
                else:
                    p1 = p1 >> 3
            else:
                p1 = p1 >> 1
        #print (bin(p1))
        if p1 == p2:
            ans = 1
            break
        
if ans:
    print ("YES")
else:
    print ("NO")
