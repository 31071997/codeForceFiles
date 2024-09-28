# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:42:56 2024

@author: ASUS
"""
x = input().split()
for i in range(0, 4):
    x[i] = int(x[i])
x.sort()
ab = x[0]
ac = x[1]
bc = x[2]
abc = x[3]
a = abc - bc
b = abc - ac
c = abc - ab
print(a, b, c)