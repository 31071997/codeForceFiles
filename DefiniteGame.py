# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:32:24 2024

@author: ASUS
"""
n = int(input())
i = n-1
while(i > 0):
   if((n%i) != 0):
     n -= i
     break
   i -= 1
print(n)