# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 04:34:28 2024

@author: ASUS
"""
n = int(input())
a = input()
u = 0
d = 0
r = 0
l = 0
for i in range(0, n):
    if(a[i] == 'U'):
        u += 1
    elif(a[i] == 'R'):
        r += 1
    elif(a[i] == 'L'):
        l += 1
    elif(a[i] == 'D'):
        d += 1
if(u < d):
    d = u
elif(u > d):
    u = d
if(r < l):
    l = r
elif(r > l):
    r = l
print(d+u+l+r)