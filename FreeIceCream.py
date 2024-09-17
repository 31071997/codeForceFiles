# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:57:21 2024

@author: ASUS
"""
n, x = input().split()
n = int(n)
x = int(x)
c = 0
for i in range(0, n):
    sign, d = input().split()
    d = int(d)
    if(sign == '+'):
        x += d
    else:
        if(d <= x):
            x -= d
        else:
            c += 1
print(x, end = " ")
print(c)