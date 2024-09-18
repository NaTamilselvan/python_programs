'''This program for try to use parent class methods in child class'''


class Customer:
    
    def __init__(self,name,ph_no,address):
        
        self.name=name
        self.ph_no=ph_no
        self.address=address
        
        
    def orderFood(self,Fooditem):
        
        cost=0
        deliverycharge=50
        
        if Fooditem=='pizza':
            
            cost = 500 + deliverycharge
            
        elif Fooditem == 'burger':
            
            cost = 500 +deliverycharge
            
        return cost
    
    
    
    
class PrimeCustomer(Customer):
    #The prmecustmer have primeid and 5 offer
    
    

     
    
    def __init__(self,name,ph_no,address,pid):
        
        super().__init__(name, ph_no, address)
        
        self.pid=pid
        
        
    def orderFood(self,Fooditem):
        
       return  super().orderFood(Fooditem)-50-0.95

         
    def __str__(self):
        return self.name



p=PrimeCustomer("Tamil", 9876544432, "Ramapuram", 1234)

print(p.orderFood("pizza"))

print(p)

