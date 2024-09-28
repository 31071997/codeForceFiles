# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 03:19:02 2024

@author: ASUS
"""
x1, x2, x3 = input().split()
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
if((x1 > x2) & (x1 < x3)):
    d = (x1-x2)+(x3-x1)
elif((x1 > x3) & (x1 < x2)):
    d = (x1-x3)+(x2-x1)
elif((x2 > x1) & (x2 < x3)):
    d = (x2-x1)+(x3-x2)
elif((x2 > x3) & (x2 < x1)):
    d = (x2-x3)+(x1-x2)
elif((x3 > x1) & (x3 < x2)):
    d = (x3-x1)+(x2-x3)
elif((x3 > x2) & (x3 < x1)):
    d = (x3-x2)+(x1-x3)
print(d)