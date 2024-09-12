def check(a):
    
    for i in a:#The range function is return s number sequence dafault 0 steps also 0
                          
        print("I check inside",i)
        if i == 5 :
            return False
        
    print("I check  outside inside")    
    return True





a=[1,2,3,4,6,5]     
print(check(a))            

