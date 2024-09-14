def power_of(ref):
    
    def wrapper(lst):
        lst=list(map(lambda  x : x**2,lst))
        ref(lst)
        
    return wrapper    



def get_product(lst):
    
    p=1
    
    for i in lst:
        
        p*=i
        
    print(p) 



k=power_of(get_product)    
k([1,2,3,4,5])