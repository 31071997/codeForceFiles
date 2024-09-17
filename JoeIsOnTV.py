# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:10:51 2024

@author: ASUS
"""
n = int(input())
i = 1
prize = 0
while(n != 0):
    prize += i/n
    n -= i 
print("%.12f" %prize)