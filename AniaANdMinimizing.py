# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:04:25 2024

@author: ASUS
"""
n, k = input().split(' ')
n = int(n)
k = int(k)
S = input()
j = 0
S = list(S)
for i in range(0, n):
    if(j < k):
        if(n == 1):
            S[i] = '0'
        elif(i == 0):
            if(int(S[i]) > 1):
                S[i] = '1'
                j += 1
        elif(int(S[i]) > 0):
            S[i] = '0'
            j += 1            
    print(S[i], end="")