#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:03:28 2024

@author: natamilme
"""

def printNthfibo(n):
    
    first,secound,thired=0,1,0
    
    while(thired<n):
        thired=first+secound
        first=secound
        secound=thired
        print(first)
        
        
    if(n==thired):
        print("FIbbonaci")
    else:
        print("Not fiboo")
    
    
    
def p(i):
    
    if i==0 or i==1 :
        return 1
    else :
            i*p(i-1)
    
    
# 0 1 1 2 3 4 5 8  
    
#printNthfibo(8)   







l=p(5) 

print(l)