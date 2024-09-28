# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:47:43 2024

@author: ASUS
"""
t = int(input())
x = input().split()
for i in range(0, t):
    x[i] = int(x[i])
    wall = 14
    if(x[i] <= wall):
        print("NO")
    else:
        x[i] %= 14
        if((x[i] == 1) | (x[i] == 2) | (x[i] == 3) | (x[i] == 4) | (x[i] == 5) | (x[i] == 6)):
            print("YES")
        else:
            print("NO")