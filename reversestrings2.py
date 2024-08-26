def countVowels(s):
    count=0
    for i in s:
        print(i)
        if i=='a' or i=='e' or i=='o' or i=='u' or i=='i' :
            count+=1
        
    
    
    print(count)
    


s=input("Enter the String\n")    

countVowels(s)
