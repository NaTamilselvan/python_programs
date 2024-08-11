#This program for to find a prime number

def findPrime(a):
    
     count=1

     for i in range(2,a):
        
        if a%i==0 :
           count+=1
           
           

     if(count==1):
        print("The number is prime number")      
     else:
        print("The number is not prime")







print(__name__)

a=int(input("Enter the a value \n"))
findPrime(a)
