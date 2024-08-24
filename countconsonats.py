def countVowels(s):
    count=0
    num=0
    consonants=0
    sp=0
    for i in s:
        #print(i)
        
        if i=='a' or i=='e' or i=='o' or i=='u' or i=='i' :
            count+=1
        else:
            consonants+=1
        
    
    
    print(count)
    print(consonants)
    


s=input("Enter the String\n")    

countVowels(s)


print(s[::-1])
