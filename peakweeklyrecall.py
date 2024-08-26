# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:02:02 2024

@author: ELCOT
"""

#GEEks For GEEKS 50 array problem 
#Peak element peak element means highest value how in asscending order last element decending order first elemnt 
#all equal value all element is peak element
#un sorted array is previews element is low next is hight after value is lower then current value 

def peakElement(ls,size):
    
    if size==1:
        return ls[0]
    elif size==2 :
         if ls[0]>ls[1]:
             return ls[0]
    elif ls[size-1]>ls[size-2]:
         return ls[size-1]
    else:
        for i in range(1,size-1) :
            if ls[i-1] <ls[i] and ls[i]>ls[i+1] :
                return ls[i]
            
    

   





ls=[5,2,3,4,5,11,6,7,8,9,1]
size=len(ls)
a=peakElement(ls,size)
print(a)

#print(len(ls))


