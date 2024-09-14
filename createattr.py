class flight:
    
    #This program for differernt way create  state of object or instance variable of object 
    
    #using __init__function
    #after object creation post object creation
    #There are build in functions
    #setattr(objectname or reference ,instance ,instace value )
    #getattr
    #also has another buildinmmethod its check for object inside here or not 
    #its for hasattr(classname,instance name)
    
    country="India"
    a=10
    b=20
    
    def __init__(self):
        self.flightName="IndianAirServicef1" 
       # self.country="India"
        self.fid=1001
        
        
    def flightstart(self):
        print(self.flightName,"Is started")
        
        
    def flightover(self):
        print(self.flightName,"Is landover")
        
    def flightflying(self):
          print(self.flightName,"Is started")  
          
    def flightlanding(self):
         print(self.flightName,"The flight is land overing")


    def display(self):
       
      print(self.flightName)
      print(self.country)
      print(self.fid) 
      print(self.flighttime)
          
        
        
 
def main():
    
    f1=flight()
    
    f1.flighttime="24 housres service"

    f1.display() 
    
    f2=flight()
    
    if(hasattr(f2,'flighttime')):
       setattr(f2, 'flightleave', "23hours")
       
    print(f1.__dict__)
    #print(f1.__dict__['country'])
       

    print(f2.__dict__)
    
    print()
    
    print()
    
    print("The classs leve variable accesss",flight.__dict__["country"])
    
    #we can access class level variable is using class name .__dict__
    print(flight.a)
    print(flight.b)
    
    f1.a=200
    f1.b=300
    
    print(f1.a)
    print(f1.b)
    
    print(flight.a)
    print(flight.b)
    
    
if __name__=='__main__':
   main()    
    
        
        

        