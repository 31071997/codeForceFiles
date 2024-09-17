# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 03:39:14 2024

@author: ASUS
"""
temp = 0
n = int(input())
while(n > 5):
    n -= 5
    temp += 1
if(n <= 5):
    temp += 1
print(temp)