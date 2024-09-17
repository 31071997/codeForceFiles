# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 04:01:21 2024

@author: ASUS
"""
n, m = input().split()
n = int(n)
m = int(m)
a = input().split()
a = list(a)
summation = 0
count = 0
for i in range(0, n):
    a[i] = int(a[i]) 
a = sorted(a)
for i in range(0, n):
    if(a[i] < 0):
        summation += abs(a[i])
        count += 1
        if(count == m):
            break
print(summation)