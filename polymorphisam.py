class A:
    
    def __init__(self,name):
        print("I am parent class constructor ")
        self.name=name
        print(self.name)

    ''' def __init__(self,name):
        
        self.name="Tamil" '''
        
        

class B(A):
    
    def __init__(self):
        print("I am B class constructor ")
        print(super().__init__("selvan") )      

    ''' def __init__(self,name):
        
        self.name="Tamil" '''
        
        
        
        
help(B)     
        