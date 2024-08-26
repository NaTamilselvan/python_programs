


def primelist(num):
    
    #print("I am enter")
    
    for i in range(3,num+1):
        
        #print("I am enter2",i)
        if num > 1 :
            
            # print("I am enter 3",num)             
             for j in range(2,i):
                 
                 if(i%j==0):
                     break;
             else :
                 print("The prime numbers is ",i)
    
    
    
    # Python program to print all
# prime number in an interval

primelist(12)



def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


