#This program for prime numbers  list from the range

def prime(x,y):
    
    list=[]

    while(x<=y):
          
         for i in  range(2,x+1):
            if i==0 or i==1:
               continue
            else:
               for j in range(2,int(x/2)+1):
                   if x%j==0 :
                      print(x,"x is not prime")
                      break;
                   
                   else:
                       list.append(x)          

    
         x+=1


    print(list)   





prime(2,10)
