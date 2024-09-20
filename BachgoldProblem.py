# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 03:04:53 2024

@author: ASUS
"""
k = int(input())
i = 1
a = []
while(k != 0):
    if(k == 3):
        a.append(3)
        k -= 3
        break
    else:
        a.append(2)
        k -= 2
    if(k != 0):
        i += 1
print(i)
print(*a)