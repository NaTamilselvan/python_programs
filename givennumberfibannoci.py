num=int(input("Enter the number"))

first,secound,c=1,1,0

if num==0 or num==1 :
    print("yes")

else:

       while(c<num):
                   
                  c=first+secound
                  first=secound
                  secound=c
                        
       if(c==num):
            print("yes")
        	else:
            print("NO")

