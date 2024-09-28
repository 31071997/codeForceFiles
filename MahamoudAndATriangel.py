# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:27:53 2024

@author: ASUS
"""
n = int(input())
a = input().split()
find = 0
for i in range(0, n):
    a[i] = int(a[i])
a = sorted(a)
for i in range(0, n-2):
    if((a[i]+a[i+1]) > a[i+2]):
        find = 1
        break
if(find == 0):
    print("NO")
else:
    print("YES")