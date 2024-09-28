# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 03:25:01 2024

@author: ASUS
"""
n = int(input())
a = []
maximum = []
num = 1
a = input().split()
for i in range(0, n):   
    a[i] = int(a[i])
for i in range(1, n):
    if(a[i] > a[i-1]):
        num += 1
    else:
        maximum.append(num)
        num = 1
if(i == n-1):
    maximum.append(num)
print(max(maximum))   