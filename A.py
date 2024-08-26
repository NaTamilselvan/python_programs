#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:08:44 2024

@author: natamilme
"""
for i in range(5):
    
    for j in range(10):
        
        if i+j==5 or j-i==5 or i==3 and j==5:
            print("*",end="")
        else:
            print(" ",end="")
    
    
    
    print()
    