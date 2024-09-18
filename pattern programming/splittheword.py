''''This program for even length of string words '''



def lengthofword():
   name="tamil"
   s=input("Enter the string\n")


   for i in s.split():
    
     if len(s)%2==0:
        print(i)
        
        
help(lengthofword)
        
        