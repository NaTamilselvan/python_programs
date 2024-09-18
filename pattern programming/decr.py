''' This program practised for colsers'''


def outer():
    
    x=10
    
    def inner():
        y=20
       # print(x)
        def inner2():
            print(x)
            print(y)
        return inner2 
          
        
    return inner





f=outer()

f2=f()
  
f2()

del outer

del f

f2()

