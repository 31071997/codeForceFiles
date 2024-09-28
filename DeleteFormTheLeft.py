# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:05:53 2024

@author: ASUS
"""
s = input()
t = input()
s = list(s)
t = list(t)
ls = len(s)
lt = len(t)
m = ls-1
n = lt-1
count  = 0
while((m >= 0) & (n >= 0)):
    if(s[m] == t[n]):
        ls -= 1
        lt -= 1
        m -= 1
        n -= 1
    else:
        break
print(ls + lt)