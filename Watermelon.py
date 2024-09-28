# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:40:37 2024

@author: ASUS
"""
w = int(input())
i = 2
y = False
if(w > 2):
    while(i <= w):
        w -= i
        if(w%2 == 0):
            print("YES")
            y = True
            break
        i += 2
if(y != True):
    print("NO")