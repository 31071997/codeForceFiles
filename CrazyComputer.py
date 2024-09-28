# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:28:31 2024

@author: ASUS
"""
n, c = input().split()
n = int(n)
c = int(c)
t = input().split()
count = 0
for i in range(0, n):
    t[i] = int(t[i])
    if(i > 0):
        if(t[i]-t[i-1] > c):
            count = 0
    count += 1
print(count)