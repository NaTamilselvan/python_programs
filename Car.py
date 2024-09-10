class car:
     
     def __init__(self):
         
          self.Name="bmv"
          self.prize=1200022
          self.color="blue"


     def start_engine(self):
    
         print(self.Name,"Engine starrted")


def main():
          
     c1=car()
     
     print(c1.Name)
     print(c1.prize)
     print(c1.color)
     
     c1.start_engine()
         
         
if __name__=="__main__":

     main()         
         
         
    