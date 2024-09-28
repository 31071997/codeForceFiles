# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:15:38 2024

@author: ASUS
"""
n, m = input().split()
n = int(n)
m = int(m)
count = 0
if(n > m):
    for a in range(0, n+1):
        for b in range(0, n+1):
             if(((pow(a, 2) + b) == n) & ((a + pow(b, 2))== m)):
                 count += 1
else:
    for a in range(0, m+1):
        for b in range(0, m+1):
             if(((pow(a, 2) + b) == n) & ((a + pow(b, 2))== m)):
                 count += 1
print(count)