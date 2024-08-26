#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:43:24 2024

@author: natamilme
"""

def reverse(l):
    start=0
    end=len(l)-1
    
    while(start<end):
        temp=l[start]
        l[start]=l[end]
        l[end]=temp
        start+=1
        end-=1
        
    print(l)




l=[10,20,30,40,50]    
reverse(l)

