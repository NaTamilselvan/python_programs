
def reverseString(s):
    
    
    length=-len(s)
    s1=""
    for i in range(-1 ,length-1,-1):
        s1=s1+s[i]
        
        
    print(s1)





s=input("Enter the String\n")    

reverseString(s)

print(s[::-1])
