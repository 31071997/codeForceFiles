# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:44:12 2024

@author: ASUS
"""
n = int(input())
a =input().split()
a = list(a)
rest = 0
store = 0
cicle = 0
for i in range(0, n):
    if(a[i] == '1'):
        rest += 1
    elif(a[i] == '0'):
        if(rest > store):
            store = rest
        rest = 0
i = 0
while (a[i] == '1'):
    rest += 1
    i += 1
if(rest > store):
    store = rest
print(store)