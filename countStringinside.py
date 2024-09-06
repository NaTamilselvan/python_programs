#This program for check given string to count no of digit ,alphabet,specialcharacters


n=input("Enter the String\n")

lower,upper,digit,special=0,0,0,0

for i in  n:
    
    if i.islower():
        lower+=1
        
    elif i.isupper():
        upper+=1
        
    elif i.isdigit():
         digit+=1
         
    else :
        special+=1
        
        
        
        
        
        
print("The  upper",upper)

print("The  lower",lower)

print("The  digit",digit) 

print("The  upper",special)       
          