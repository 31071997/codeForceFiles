# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:44:29 2024

@author: ASUS
"""
for i in range(0, 5):
    n = input().split()
    for j in range(0, 5):
        n[j] = int(n[j])
        if(n[j] == 1):
            c = j
            r = i
if(c!= 2):
    c = abs(2 - c)
else:
    c = 0
if(r!= 2):
    r = abs(2 - r)
else:
    r = 0
print(r+c)