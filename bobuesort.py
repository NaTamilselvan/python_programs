def add():
    """ This program for add two numbers """
    


a=[21,45,32,67,45,78]


for i in range(len(a)):
    
    for j in range (len(a)-i-1):
         
       if a[j]>a[j+1]:
           
           a[j],a[j+1]=a[j+1],a[j]
           
           
           
print(a)           