# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:32:49 2024

@author: ASUS
"""
a, b = input().split()
a = int(a)
b = int(b)
i = 1
while (a <= b):
    a *= 3
    b *= 2
    i += 1
print(i-1)
    