
""" This program for i am trying to  list comprehension 
list comprehension is nothing but provides simple syntex while 
creating a new list from existing list besed on some condtion
"""

animals=["lion", "tigher", "monkey", "elephant", "frog"]

flitered_Animals=[]

for i in animals:
    
    flitered_Animals.append(i.title())
    
    
print(flitered_Animals)

#sames as list comprehension to make one line:
    
k=[name.title()  for name in animals]

print(k)
    