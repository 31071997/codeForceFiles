# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 00:27:51 2024

@author: ASUS
"""
n, m = input().split()
n = int(n)
m = int(m)
count = 0
for i in range(0, n):
    if(i%2 == 0):
        for j in range(0, m):
            if(j != (m-1)):
                print("#", end="")
            else:
                print("#")
    else:
        if(count%2 == 0):
            for k in range(0, m-1):
                print(".", end="")
            print("#")
            count += 1
        else:
            print("#", end="")
            for k in range(1, m):
                if(k != (m-1)):
                    print(".", end="")
                else:
                    print(".")
            count += 1