# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 02:51:30 2024

@author: ASUS
"""
t = int(input())
for i in range(0, t):
    n = int(input())
    a = input().split()
    a = list(a)
    for j in range(0, n):
        a[j] = int(a[j])
    for j in range(0, n):
        if(j == (n - 1)):
            print(a[0])
        else:
            amax = max(a)
            print(amax, end=" ")
            a.remove(amax)