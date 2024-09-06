

s=input("Enter the String\n")

s2=""
for i in s:
    
    if i.islower() :
        if i=='a ' or i=='e' or i=='i' or i=='o' or i=='u':
           s2+= chr(ord(i)-32)
        else:
             s2+=i   
           
    elif i.upper():
            s2+=i
            
    elif i.isnumeric():
            s2+=""
    else:
        s2+=i







print(s2)            
            
            
            
        
        