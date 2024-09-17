class Error(Exception):
    pass

class lowvalueError(Error):
    pass

class highestvalue(Error):
    pass

num=10

while True:
    
     try:

      ch=int(input("Enter the number\n "))
      if ch<10:
        raise lowvalueError    
      elif ch>10:
         raise  highestvalue   
      break  
        
     except lowvalueError as l:
        print("You enter low value ")
     except highestvalue as h:
           print("You enter high value ")     
           
print("you enter correct value")           