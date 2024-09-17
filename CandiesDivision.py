# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:12:33 2024

@author: ASUS
"""
t = int(input())
for i in range(0, t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    half = int(k/2)
    extra = n%k
    if(extra == 0):
        print(n)
    else:
        n = int(n/k)*k
        if(extra >= half):
            print(n + half)
        else:
            print(n + extra)