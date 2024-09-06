x=[
   
   [1,2,3],
   [2,3,4],
   [5,6,7]
   
   
   ]

#another one matrix
y=[
   
   [1,2,3],
   [2,3,4],
   [5,6,7]
   
   
   ]

#Its another one result matrix

z=[
   
   [0,0,0],
   [0,0,0],
   [0,0,0]
   
   
   ]



for i in range(len(x)):
    #ITs trversal to row 
    
      for j in range(len(x[0])):
          
          z[i][j]=x[i][j]+y[i][j]
    
      print()
      
      
     
        
print(z)    