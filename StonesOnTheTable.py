# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:44:08 2024

@author: ASUS
"""
n = int(input())
s = list(input())
count = 0
for i in range(1, n):
    if(s[i] == s[i-1]):
        count += 1
print(count)