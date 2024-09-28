# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:21:35 2024

@author: ASUS
"""
n = int(input())
a = input().split()
a = list(a)
count = 0
average = 0
for i in range(0, n):
    a[i] = int(a[i])
while(1):
    average = sum(a)/n
    if(average >= 4.5):
        average = 5
    if(average >= 5):
        break
    else:
        a[a.index(min(a))] = 5
    count += 1
print(count)