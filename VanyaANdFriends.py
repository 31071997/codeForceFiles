# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:20:55 2024

@author: ASUS
"""
n, h = input().split()
n = int(n)
h = int(h)
width = 0
b = []
a = input().split()
for i in range(0, n):
    b.append(int(a[i]))
for i in range(0, n): 
    if(b[i] > h):
        width += 2
    else:
        width += 1
print(width)