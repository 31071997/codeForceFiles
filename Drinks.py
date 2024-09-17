# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:59:03 2024

@author: ASUS
"""
n = int(input())
s = 0
p = input().split()
for i in range(0, n):
    p[i] = int(p[i])
    s += p[i]
print(s/n)