# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:55:08 2024

@author: ASUS
"""
k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)
cost = 0
for i in range(1, w+1):
    cost += i*k
if(cost < n):
    print(0)
else:
    loan = cost - n
    print(loan)