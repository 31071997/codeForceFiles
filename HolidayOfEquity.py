# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:48:06 2024

@author: ASUS
"""
def maxNum(x):
    m = x[0]
    for i in range(1, len(x)):
        if(x[i] > m):
            m = x[i]
    return m
n = int(input())
a = input().split()
for i in range(0, n):
    a[i] = int(a[i])
Max = maxNum(a)
S = 0
for i in range(0, n):
    if(a[i] < Max):
        S += (Max-a[i])
print(S)