class Car:
    
    #class method is a method call it return a object 
    #class method accespt input as cls it means class name 
     
    def bmw(cls):
        return Car("x8","2lack","blue")
    
    
    @staticmethod
    def register():
        print("Its car is india car")
    
    
    def __init__(self,name,prise,color):

            self.name=name
            self.prise=prise
            self.color=color
            
    #instance method is a depend on object.its behaviour of object
    #instance method first argument aleasy self keyword
    def display(self):
        print(self.name)
        print(self.prise)
        print(self.color)
    
    
def main():
    
    c1=Car("bmw","onelacak","black")
    #internally it convert is Car(c1,"bmw","onelack","black)
    c1.display()
    
    print(c1.__dict__)
    Car.register()
    c1.register()#car(c1)
    
    c2=Car.bmw(Car)
    
    c2.display()
    
    
    
if __name__=="__main__":

    main()

    
    
                
        