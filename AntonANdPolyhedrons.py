# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 04:20:34 2024

@author: ASUS
"""
n = int(input())
plane = 0
for i in range(0, n):
    s = input()
    if(s == "Tetrahedron"):
        plane += 4
    if(s == "Cube"):
        plane += 6
    if(s == "Octahedron"):
        plane += 8
    if(s == "Dodecahedron"):
        plane += 12
    if(s == "Icosahedron"):
        plane += 20
print(plane)