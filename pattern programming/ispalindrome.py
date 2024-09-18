def ispalindrome(s):
    
    
    for i in range(len(s)//2):
        
        for j in range(-1,-len(s)//2-1,-1):
            
            print("s[i] value ",s[i],"s[j] value",s[j])
            if s[i]==s[j]:
               break
           




s="malayalam"


ispalindrome(s)

if  s == s[::-1] :
    print("This string is palindrome")
    
else:
    print("This string is not palindrome")    