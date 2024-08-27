s=input("Enter the string\n")


j=len(s)-1;
for i in range(len(s)//2):
    
    if (s[i]!=s[j]):
        print("Not palindrome")
        break
    j-=1
    
else:
     
    print("The string is palindrome")    
    
    
    
    
print(len(s)//2)   