#This program for practise object creation

class FootBaller:
    
    
    def __init__(self,name ,country,goals):
        
        self.name=name
        self.country=country
        self.goals=goals
        
        
        
    def Enter(self):
        print(self.name,"Enter the match")
        
    def trykick(self):
        print(self.name ,"try to kic")
    def achieveGoal(self):
         print(self.country ,"acheieve one point",self.goals)
     
         
     
        
def main():

   ronalto= FootBaller("ronalto","strick",988)#internally to conversion
   #ronalto=FootBaller(self,ronalto,"strick",988)
   ronalto.Enter()
   
   ronalto.achieveGoal()
   
   
   
if __name__=="__main__":
    
    main()
    
    
   
   
        
        
        