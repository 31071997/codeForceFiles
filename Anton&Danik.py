# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:58:48 2024

@author: ASUS
"""
n = int(input())
s = input()
a = 0
d = 0
for i in range(n):
    if(s[i] == 'A'):
        a += 1
    else:
        d += 1
if(a > d):
    print("Anton")
elif(d > a):
    print("Danik")
else:
    print("Friendship")