# -*- coding: utf-8 -*-
"""
Created on Mon May 20 19:51:11 2024

@author: ASUS
"""
n = int(input())
i = 1    
t = 0
while(t < n):
    t = (i*(i+1))/2
    if(t == n):
        print("YES")
        break
    i+=1
if(t > n):
    print("NO")
    