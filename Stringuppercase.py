S="Python developer "

s2=""

for i in S:
    
    if ord(i)>=97 and ord(i)<=122:
        
        s2+=chr(ord(i)-32)
        
    else:
        s2+=i
        
        
        
        
        
print(s2)        