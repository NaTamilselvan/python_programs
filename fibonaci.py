#This program is for fibonaci

def fibonacci(n):
      f=0
      s=1      
      for i in range(n):
              print(f,end="  ")
              thired=f+s
              f=s
              s=thired
 



fibonacci(11)