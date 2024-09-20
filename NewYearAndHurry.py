# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:02:12 2024

@author: ASUS
"""
def time(a, b):
    t = 0
    for i in range(1, a+1):
        t += i*5
        if(t == b):
            return i
        elif(t > b):
            return i-1
    if(i == n):
        return n    
n, k = input().split()
n = int(n)
k = int(k)
k = (4*60)-k
print(time(n,k))
