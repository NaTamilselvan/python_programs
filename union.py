def  findunion(a,b):
      
     lista=[]
     listb=[]
     n=len(a)
     m=len(b)     

     for i in a:
        b=False
        for j in b:
          if(a[i]==b[j]):
              lista.append(a[i])
              b=True   
              break
           
        if(b==True):
          listb.append(b[i]) 
      
     for k in lista:
         print(lista[i])
     for l in lista:
         print(listb[i])


#driver code:
arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
findunion(arr1,arr2)  

