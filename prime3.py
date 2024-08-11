#This program is i find a prime number

def Prime(q,k):

   while(q<=k):
    
    bool=True
    for i in range(2, q+1):
        
          if q%i==0 :
              bool=False
              break;
           
    if bool==True :
       print("This number",q,"is prime number")
    else:
       print("This number ",q,"is not prime")

    q=q+1

n=int(input("Enter the number  n \n"))
k=int(input("Enter the number  k \n"))
Prime(n,k)   
