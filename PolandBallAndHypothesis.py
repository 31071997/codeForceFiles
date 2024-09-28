# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 02:23:59 2024

@author: ASUS
"""
def prime(a):
    for i in range(2, a-1):
        if(a%i == 0):
            return False
    return True
n = int(input())
for m in range(1, 1000):
    if(prime((n*m)+1)==False):
        print(m)
        break