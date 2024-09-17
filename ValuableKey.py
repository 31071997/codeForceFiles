# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:52:54 2024

@author: ASUS
"""
x = input()
y = input()
x = list(x)
y = list(y)
z = []
l = len(x)
result = ""
mark = 1
for i in range(0, l):
    if(y[i] < x[i]):
        z.append(y[i])
    elif(y[i] == x[i]):
        z.append(x[i])
    else:
        mark = 0
        break
    result += z[i]
if(mark == 1):
    print(result)
else:
    print(-1)