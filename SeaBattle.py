# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 01:21:05 2024

@author: ASUS
"""
w1, h1, w2, h2 = input().split()
w1 = int(w1)
h1 = int(h1)
w2 = int(w2)
h2 = int(h2)
if(w1 == w2):
    print((2*w1)+(2*(h1+h2))+4)
else:
    print(w1+w2+(2*(h1+h2))+(w1-w2)+4)