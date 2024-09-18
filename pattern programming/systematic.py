def isSystematic(s):
    
    l=len(s)
    
    
    if l%2==0:
        mid=len(s)//2
         
        return s[:mid]==s[mid:]
    else:
        return s[:mid]==s[mid+1:]
        


s=input("Enter the string\n")


result=isSystematic(s)


if (result):
    print("This systematic string")
    
else:
    print("not systemmatic")
        
