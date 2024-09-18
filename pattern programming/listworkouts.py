lst=['tamil','selvan','python','developer']

lst2=lst

print(lst)

print(lst2)


print(lst is lst2)

for i in range(len(lst)):
    
    print("The first lst",id(lst[i])," ","The secound lst2",id(lst2[i]))
    
    
   
    
lst3=lst[:]

print(lst3)


print(lst is lst3)  
    

for i in range(len(lst)):
    
    print("The first lst",id(lst[i])," ","The secound lst2",id(lst3[i]))
    