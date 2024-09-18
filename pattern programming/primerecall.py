def prime(x,y):
    
   prime_list=[] 
   for j in range(x,y+1):  
       
      if j==0 or j==1 :
         continue
     
      else :   
    
       for i in range(2,int(j//2)+1):
        
         if j%i == 0:
            break
        
        
        
       else:
        
         prime_list.append(j)  

        

   return prime_list

      
      
      


l=prime(1,20)


if len(l) == 0 :
    
    print("no prime number")
    
    
else:
     
    print("The prime number are ",l)    
      